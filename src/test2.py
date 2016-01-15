# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb

if __name__ == "__main__":
    from src.common.rabbitmq import publisher

    a = publisher.Publisher('zabbix_event_queue')
    aaa = 'sadasdasd'
    a.send(aaa)