# -*- coding:utf-8 -*-
import sys
import os
import json

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from src.main_event.pattern_process import *
from src.common.redis import queue

cum = queue.InitQ('zabbix_event_queue')

warning_dict = {'ip': '10.4.11.82','description':'111','type_id':4,'kind_id':1,'status':'PROBLEM'}
print warning_dict
print cum.rpush(json.dumps(warning_dict))