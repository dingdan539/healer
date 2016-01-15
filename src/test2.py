# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb
from src.common.rabbitmq import publisher
if __name__ == "__main__":

    a = publisher.Publisher('zabbix_event_queue')
    aaa = 'sadasdasd'
    a.send(aaa)