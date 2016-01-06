# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import src.function.basic as fb
import time

"""所有类都必须是互斥的，满足一个不满足别的"""


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


# class ProcessDirect(Father, InterfaceOutPut):
#     def process(self, warning_dict):
#         source_id = warning_dict['source_id']
#         type_id = warning_dict['type_id']
#         if