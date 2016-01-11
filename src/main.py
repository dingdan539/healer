# -*- coding:utf-8 -*-

import sys
from config import *

if __name__ == "__main__":

    config = load_config_auto()

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sys.path.append(ROOT_PATH)

    from src.main_event.assemble import *
    from src.common.db.op import *
    from src.common.rabbitmq import consumer

    #cum = consumer.Consumer('zabbix_event_queue')

    warning_dict = dict()
    warning_dict['description'] = """10.4.11.82PROBLEM: tomcat port 8080 can't connectvalue:0;_Trigger: tomcat port 8080 can't connect"""
    # 10.4.11.82 10.4.43.176
    warning_dict['clock'] = 12345678
    warning_dict['host_name'] = " empty"
    warning_dict['source_id'] = 1

    a = ZabbixAnalyse()
    a.analyse(warning_dict)
    # def fun(body):
    #     a.analyse(body)
    #
    # cum.receive(fun)