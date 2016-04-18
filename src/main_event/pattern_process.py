# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import src.function.basic as fb
import time


class Main(Father):
    def nc_check(self, warning_dict, ip, port, c_time=2):
        if not ip and not warning_dict['ip']:
            return True
        else:
            tag = 0
            for i in range(0, c_time):

                cmdstr = r'''nc -z -vv -w 1 ''' + ip + ''' ''' + str(port)
                print cmdstr
                code, stdout, stderr = fb.command(cmdstr)
                print code, stdout, stderr
                if code != 1:
                    tag = 1
                    break
                time.sleep(0.1)

            if tag == 0:
                warning_dict['remark'] = stderr
                kwargs = {
                    'tb_name': 'important_event',
                    'field': warning_dict
                }
                res = self.f_ie_db.insert(**kwargs)
                print res
            return True



"""所有类都必须是互斥的，满足一个不满足别的"""


class ProcessZabbixFilter(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点 (预处理函数，永远返回false)"""
    def process(self, warning_dict):
        kind_id = warning_dict['kind_id']
        if kind_id != 1:
            return True
        else:
            return False


class ProcessZabbixTomcat(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 4) and (status == 'PROBLEM'):
            cmdstr = r'''nc -z -vv -w 1 ''' + ip + ''' 8080'''
            code, stdout, stderr = fb.command(cmdstr)
            if code == 1:
                time.sleep(0.1)
                code, stdout, stderr = fb.command(cmdstr)
                if code == 1:
                    warning_dict['remark'] = stderr
                    kwargs = {
                        'tb_name': 'important_event',
                        'field': warning_dict
                    }
                    self.f_ie_db.insert(**kwargs)
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
            cmdstr = r'''nc -z -vv -w 1 ''' + ip + ''' 80'''
            code, stdout, stderr = fb.command(cmdstr)
            if code == 1:
                time.sleep(0.1)
                code, stdout, stderr = fb.command(cmdstr)
                if code == 1:
                    warning_dict['remark'] = stderr
                    kwargs = {
                        'tb_name': 'important_event',
                        'field': warning_dict
                    }
                    self.f_ie_db.insert(**kwargs)
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