# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import os
import time

class ProcessZabbixTomcat(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 4) and (status == 'PROBLEM'):
            res = os.popen(r'''nc -z -vv -w 1 ''' + ip + ''' 8080''').read()
            if 'succeeded' not in res:
                time.sleep(0.1)
                res = os.popen(r'''nc -z -vv -w 1 ''' + ip + ''' 8080''').read()
                print 111111111111111
                print res
                if 'succeeded' not in res:
                    warning_dict['remark'] = res
                    print warning_dict
                    kwargs = {
                        'tb_name': 'important_event',
                        'field': warning_dict
                    }
                    self.f_ie_db.insert(**kwargs)
            return True
        else:
            return False