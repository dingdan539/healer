# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import time
import threading


class ProcessZabbixStability(Father, InterfaceOutPut):
    window_view = dict()

    def scan_count(self):
        """循环检测是否触发报警阀值"""
        while 1:
            for i in self.window_view:
                if self.window_view[i]['count'] >= 3:
                    self.window_view[i]['count'] = 0
                    self.window_view[i]['time'] = int(time.time())

                    self.window_view[i]['field']['remark'] = 'count >= 3'

                    kwargs = {
                        'tb_name': 'important_event',
                        'field': self.window_view[i]['field']
                    }
                    self.f_ie_db.insert(**kwargs)

                elif (int(time.time()) - self.window_view[i]['time']) > 60:
                    self.window_view[i]['count'] = 0
                    self.window_view[i]['time'] = int(time.time())

            time.sleep(1)

    def process(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        if type_id != 0:
            if type_id not in self.window_view:
                if status == 'PROBLEM':
                    self.window_view.setdefault(type_id, {})
                    self.window_view[type_id]['count'] = 1
                    self.window_view[type_id]['time'] = int(time.time())
                    self.window_view[type_id]['field'] = warning_dict
            else:
                if status == 'PROBLEM':
                    self.window_view[type_id]['count'] += 1
                    self.window_view[type_id]['time'] = int(time.time())
                    self.window_view[type_id]['field'] = warning_dict
                elif status == 'OK':
                    if self.window_view[type_id]['count'] != 0:
                        self.window_view[type_id]['count'] -= 1
                        self.window_view[type_id]['time'] = int(time.time())
                        self.window_view[type_id]['field'] = warning_dict