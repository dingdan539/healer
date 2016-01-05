# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *


class ProcessZabbixTomcat(Father, InterfaceOutPut):
    """必须有返回bool True - 执行并break False - 寻找下一个执行点"""
    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        ip = warning_dict['ip']
        if (type_id == 4) and (status == 'PROBLEM'):

            return True
        else:
            return False