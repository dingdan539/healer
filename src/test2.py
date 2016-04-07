# -*- coding:utf-8 -*-

import sys
import json
import route.docs_route as r_docs
from config import *

if __name__ == "__main__":
    # config = load_config_auto()
    #
    # ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #
    # sys.path.append(ROOT_PATH)
    #
    # # from src.main_event.assemble import *
    # from src.common.redis import queue
    #
    # cum = queue.InitQ('zabbix_event_queue')
    #
    # aa = "123"
    # print cum.rpush(aa)
    class A(object):
        ss = 1

    class B(A):
        cc = 2

    b = B()
    print dir(b)

