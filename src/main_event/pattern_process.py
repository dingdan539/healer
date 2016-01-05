# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import src.function.basic as fb
import os
import time

class ProcessZabbixTomcat(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 4) and (status == 'PROBLEM'):
            cmdstr = r'''nc -z -vv -w 1 ''' + ip + ''' 8080'''
            code, stdout, stderr = fb.command(cmdstr)
            if 'succeeded' not in stdout:
                time.sleep(0.1)
                code, stdout, stderr = fb.command(cmdstr)
                if 'succeeded' not in stdout:
                    warning_dict['remark'] = stdout
                    print warning_dict
                    kwargs = {
                        'tb_name': 'important_event',
                        'field': warning_dict
                    }
                    self.f_ie_db.insert(**kwargs)
            return True
        else:
            return False