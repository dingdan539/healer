# -*- coding:utf-8 -*-
from ...function.decorator import *
from father import *

def a():
    print 'a-'

# @singleton
# class DbOp(object):
#     def __init__(self, tag, **kwargs):
#         print 'init:' + tag
#         return Db(**kwargs)