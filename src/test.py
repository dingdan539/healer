# -*- coding:utf-8 -*-
import sys
import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)

from src.main_event.pattern_process import *

warning_dict = {'ip': '10.4.11.82','description':'111'}
a = Main()
a.nc_check(warning_dict, '', 8080, 2)