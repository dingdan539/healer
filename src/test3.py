# -*- coding:utf-8 -*-
import time
import threading


class ProcessZabbixStability(object):
    window_view = dict()

    def scan_count(self):
        """循环检测是否触发报警阀值"""
        while 1:
            print self.window_view
            for ip in self.window_view:
                for type_id in self.window_view[ip]:
                    if self.window_view[ip][type_id]['count'] >= 3:
                        self.window_view[ip][type_id]['count'] = 0
                        self.window_view[ip][type_id]['time'] = int(time.time())

                        self.window_view[ip][type_id]['field']['remark'] = 'count >= 3'
                        print 'ccccccccccccccccccccccccccccccccccccccccc'
                        # kwargs = {
                        #     'tb_name': 'important_event',
                        #     'field': self.window_view[ip][type_id]['field']
                        # }
                        # self.f_ie_db.insert(**kwargs)

                    elif (int(time.time()) - self.window_view[ip][type_id]['time']) > 20:
                        self.window_view[ip][type_id]['count'] = 0
                        self.window_view[ip][type_id]['time'] = int(time.time())

            time.sleep(1)

    def process(self, warning_dict):
        ip = warning_dict['ip']
        type_id = warning_dict['type_id']
        status = warning_dict['status']
        if (type_id != 0) and ip:
            if ip not in self.window_view:
                self.window_view.setdefault(ip, {})
            if type_id not in self.window_view[ip]:
                if status == 'PROBLEM':
                    self.window_view[ip].setdefault(type_id, {})
                    self.window_view[ip][type_id]['count'] = 1
                    self.window_view[ip][type_id]['time'] = int(time.time())
                    self.window_view[ip][type_id]['field'] = warning_dict
            else:
                if status == 'PROBLEM':
                    self.window_view[ip][type_id]['count'] += 1
                    self.window_view[ip][type_id]['time'] = int(time.time())
                    self.window_view[ip][type_id]['field'] = warning_dict
                elif status == 'OK':
                    if self.window_view[ip][type_id]['count'] != 0:
                        self.window_view[ip][type_id]['count'] -= 1
                        self.window_view[ip][type_id]['time'] = int(time.time())
                        self.window_view[ip][type_id]['field'] = warning_dict

ww1 = {'ip': '1.1.1.1', 'type_id': 2, 'status': 'PROBLEM'}
ww2 = {'ip': '1.1.1.1','type_id': 2, 'status': 'PROBLEM'}
ww3 = {'ip': '1.1.1.1','type_id': 2, 'status': 'OK'}
ww4 = {'ip': '1.1.1.1','type_id': 2, 'status': 'PROBLEM'}
ww5 = {'ip': '1.1.1.1','type_id': 2, 'status': 'PROBLEM'}
ww6 = {'ip': '1.1.1.1','type_id': 2, 'status': 'OK'}
ww7 = {'ip': '1.1.1.1','type_id': 2, 'status': 'OK'}
ww8 = {'ip': '1.1.1.1','type_id': 2, 'status': 'OK'}

ww9 = {'ip': '1.1.1.1','type_id': 2, 'status': 'PROBLEM'}
ww10 = {'ip': '1.1.2','type_id': 2, 'status': 'PROBLEM'}
ww11 = {'ip': '1.1.2','type_id': 2, 'status': 'PROBLEM'}
ww12 = {'ip': '1.1.2','type_id': 2, 'status': 'PROBLEM'}

ll = [ww1,ww2,ww3,ww4,ww5,ww6,ww7,ww8,ww9,ww10,ww11,ww12]
aa = ProcessZabbixStability()

threadpool = None

th = threading.Thread(target=aa.scan_count)
threadpool = th
th.start()


for inum in ll:
    aa.process(inum)
    time.sleep(1)
