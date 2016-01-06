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

    import threading
    from time import sleep
    from json import *

    b = ZabbixAnalyse()

    warning_dict = dict()
    warning_dict['description'] = """
    10.4.11.82PROBLEM: tomcat port 8080 can't connectvalue:0;_Trigger: tomcat port 8080 can't connect
    """
    # 10.4.11.82 10.4.43.176
    warning_dict['clock'] = 12345678
    warning_dict['host_name'] = " empty"
    warning_dict['source_id'] = 1

    n = b.analyse(warning_dict)

    warning_dict = dict()
    warning_dict['description'] = """
    10.4.11.44PROBLEM: Net traffic Utilization is more than 600Mb/s on hadoop-11-44 i
    """
    # 10.4.11.82 10.4.43.176
    warning_dict['clock'] = 12345678
    warning_dict['host_name'] = " empty"
    warning_dict['source_id'] = 1

    n = b.analyse(warning_dict)

    # warning_dict2 = dict()
    # warning_dict2['description'] = """
    #     10.41.11.1OK: tomcat port 8080 can't connectvalue:0;_Trigger: tomcat port 8080 can't connect
    # """
    # warning_dict2['clock'] = 12345678
    # warning_dict2['host_name'] = "10.41.11.1_bj_ping_check"
    #
    # ll = [warning_dict, warning_dict2]

    # threadpool=[]
    # f=file("hello.txt","w+")
    # def test(nloop, ww):
    #     b = ZabbixAnalyse()
    #     nbb = b.analyse(ww)
    #     print nbb
    #     f.write(JSONEncoder().encode(nbb))
    #     f.write("\n")
    #
    # for i in ll:
    #     th = threading.Thread(target= test,args= (2, i))
    #     threadpool.append(th)
    #
    # for th in threadpool:
    #     th.start()
    #
    # for th in threadpool :
    #     threading.Thread.join( th )