# -*- coding:utf-8 -*-
import time
import threading


class ProcessZabbixStability(object):
    window_view = dict()

    def scan_count(self):
        """循环检测是否触发报警阀值"""
        while 1:
            for i in self.window_view:
                print self.window_view[i]
                if self.window_view[i]['count'] >= 3:
                    self.window_view[i]['count'] = 0
                    self.window_view[i]['time'] = int(time.time())

                    self.window_view[i]['field']['remark'] = 'count >= 3'

                    print i, 'count >=3'
                    # kwargs = {
                    #     'tb_name': 'important_event',
                    #     'field': self.window_view[i]['field']
                    # }
                    # self.f_ie_db.insert(**kwargs)

                elif (int(time.time()) - self.window_view[i]['time']) > 60:
                    print i, 'time > 60 init'
                    self.window_view[i]['count'] = 0
                    self.window_view[i]['time'] = int(time.time())

            time.sleep(1)

    def send(self, warning_dict):
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        print 'send~~~~'
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

ww1 = {'type_id': 2, 'status': 'PROBLEM'}
ww2 = {'type_id': 2, 'status': 'PROBLEM'}
ww3 = {'type_id': 2, 'status': 'OK'}
ww4 = {'type_id': 2, 'status': 'PROBLEM'}
ww5 = {'type_id': 2, 'status': 'PROBLEM'}
ww6 = {'type_id': 2, 'status': 'OK'}
ww7 = {'type_id': 2, 'status': 'OK'}
ww8 = {'type_id': 2, 'status': 'OK'}

ww9 = {'type_id': 2, 'status': 'PROBLEM'}
ww10 = {'type_id': 2, 'status': 'PROBLEM'}
ww11 = {'type_id': 2, 'status': 'PROBLEM'}
ww12 = {'type_id': 2, 'status': 'PROBLEM'}

ll = [ww1,ww2,ww3,ww4,ww5,ww6,ww7,ww8,ww9,ww10,ww11,ww12]
aa = ProcessZabbixStability()

threadpool = None

th = threading.Thread(target=aa.scan_count)
threadpool = th
th.start()


for inum in ll:
    aa.send(inum)
    time.sleep(1)
