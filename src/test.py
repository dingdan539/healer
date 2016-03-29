# -*- coding:utf-8 -*-
import datetime
import time
import function.basic as fb
from function.class_method import create


start_time = 99
duration = 1
end_time = start_time + (duration if duration else 3600)
print end_time