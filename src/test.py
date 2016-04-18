# -*- coding:utf-8 -*-
import sys
import os
import json

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from src.main_event.pattern_process import *
from src.common.redis import queue
print type((1, 'a'))
a = (1, 'a')
print a[0]
# cum = queue.InitQ('zabbix_event_queue')
#
# warning_dict = {'description':'10.4.11.82PROBLEM: tomcat port 8080','source_id':1,'clock':1460962171}
# print warning_dict
# print cum.rpush(json.dumps(warning_dict))