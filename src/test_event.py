# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(ROOT_PATH)
    from src.common.db import op
    from src.main_event.assemble import *

    warning_dict = dict()
    warning_dict['description'] = """
        10.4.5.122OK: tomcat port 8080 can't connectvalue:0;_Trigger: tomcat port 8080 can't connect
    """
    warning_dict['clock'] = 12345678
    warning_dict['host_name'] = "10.152.1.200_bj_ping_check"

    b = ZabbixAnalyse()
    b.analyse(warning_dict)
