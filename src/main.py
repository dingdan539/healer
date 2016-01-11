# -*- coding:utf-8 -*-

import sys
import json
from config import *

if __name__ == "__main__":

    config = load_config_auto()

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sys.path.append(ROOT_PATH)

    from src.main_event.assemble import *
    from src.common.rabbitmq import consumer

    cum = consumer.Consumer('zabbix_event_queue')

    a = ZabbixAnalyse()

    def fun(body):
        a.analyse(json.loads(body))

    cum.receive(fun)