# -*- coding:utf-8 -*-
import sys
import os
import json

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from src.main_event.pattern_process import *
from src.function.class_method import *
from src.common.redis import queue


#
# cum = queue.InitQ('zabbix_event_queue')
#
# warning_dict = {'description':'1.1.1.11PROBLEM: tomcat port 8080','source_id':1,'clock':1460962171}
# print warning_dict
# print cum.rpush(json.dumps(warning_dict))

# a = Main()
# res = a.sys_check(warning_dict, '10.17.26.185', 0, 2, 'ping')
# print res
# res = a.sys_check(warning_dict, '10.17.26.184', 0, 2, 'ping')
# print res


# root_child_path = '/route/docs_route.py'
# root_api_path = os.getcwd() + root_child_path
#
# fh = open(root_api_path)
# for line in fh.readlines():
#     print line
