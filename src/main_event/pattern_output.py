# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import time
import json


class OutputZabbix(Father, InterfaceOutPut):
    def output(self, warning_dict):
        kwargs = {
            'tb_name': 'alert_' + time.strftime('%Y'),
            'field': warning_dict
        }
        self.f_ie_db.insert(**kwargs)


class OutputMqStability(Father, InterfaceOutPut):
    def output(self, warning_dict):
        kind_id = warning_dict['kind_id']
        if kind_id == 2:
            self.f_stb_p_q.send(json.dumps(warning_dict))