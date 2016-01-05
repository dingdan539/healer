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
        return self.f_ie_db.insert(**kwargs)