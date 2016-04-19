# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import src.function.basic as fb
import time


class Main(Father):
    reason_map = {
        0: 'not found',
        1: 'nc检测失败',
        2: 'hc检测失败',
        3: '虚拟机可能挂了',
        4: '物理机可能挂了',
        5: '交换机可能挂了',

    }

    def insert_db(self, warning_dict, reason_id=0, stderr=''):
        warning_dict['remark'] = stderr
        warning_dict['probably_id'] = reason_id
        warning_dict['probably_reason'] = self.reason_map.get(reason_id, '')
        kwargs = {
            'tb_name': 'important_event',
            'field': warning_dict
        }
        self.f_ie_db.insert(**kwargs)

    def sys_check(self, warning_dict, ip, port, c_time=2, style='nc'):
        if not ip and not warning_dict['ip']:
            return False
        else:
            if not ip:
                ip = warning_dict['ip']
            tag = 0
            if style == 'nc':
                cmdstr = r'''nc -z -vv -w 1 ''' + ip + ''' ''' + str(port)
            elif style == 'ping':
                cmdstr = r'''ping -c 1 ''' + ip
            else:
                return False
            for i in range(0, c_time):
                code, stdout, stderr = fb.command(cmdstr)
                if code != 1:
                    tag = 1
                    break
                time.sleep(0.1)

            if tag == 0:
                return (1, stderr)
            return False


"""所有类都必须是互斥的，满足一个不满足别的"""


class ProcessZabbixFilter(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点 (预处理函数，永远返回false)"""
    def process(self, warning_dict):
        kind_id = warning_dict['kind_id']
        if kind_id != 1:
            return True
        else:
            return False


class ProcessZabbixTomcat(Main, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 4) and (status == 'PROBLEM'):
            res = self.sys_check(warning_dict, ip, 8080, 3)
            if res:
                self.insert_db(warning_dict, res[0], res[1])
            return True
        else:
            return False


class ProcessZabbixSquidPort(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 11) and (status == 'PROBLEM'):
            res = self.sys_check(warning_dict, ip, 80, 3)
            if res:
                self.insert_db(warning_dict, res[0], res[1])
            return True
        else:
            return False


class ProcessDirect(Father, InterfaceOutPut):
    """以上都没匹配到，就直接推入"""
    def process(self, warning_dict):
        kind_id = warning_dict['kind_id']
        status = warning_dict['status']
        if (kind_id == 1) and (status != 'OK'):
            kwargs = {
                'tb_name': 'important_event',
                'field': warning_dict
            }
            self.f_ie_db.insert(**kwargs)
            return True
        else:
            return False