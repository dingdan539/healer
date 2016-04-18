# -*- coding:utf-8 -*-
import sys
import os
from src.main_event.pattern_process import *
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

warning_dict = {'ip': '10.4.11.82','description':'111'}
a = Main()
a.nc_check(warning_dict, '', 8080, 2)