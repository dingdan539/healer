# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import time


class OutputZabbix(Father, InterfaceOutPut):
    def output(self, warning_dict):
        kwargs = {
            'tb_name': 'alert_' + time.strftime('%Y'),
            'field': warning_dict
        }
        self.f_ie_db.insert(**kwargs)


class OutputMqStability(Father, InterfaceOutPut):
    def output(self, warning_dict):
        kind_map = warning_dict['kind_map']
        if kind_map == 2:
            self.f_stb_p_q.send(warning_dict)