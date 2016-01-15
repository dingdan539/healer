# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb

if __name__ == "__main__":
    config = load_config_auto()

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sys.path.append(ROOT_PATH)

    from src.common.rabbitmq import publisher

    a = publisher.Publisher('zabbix_event_queue')
    aaa = 'sadasdasd'
    a.send(aaa)