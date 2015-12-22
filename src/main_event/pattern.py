# -*- coding:utf-8 -*-
from interface import *
from ..function.decorator import *
from ..common.db.op import *


class Father(object):
    ie_db = None  # intelligent_event db 句柄
    kind_map = None
    level_map = None
    source_map = None
    type_map = None

    def __init__(self):
        self.ie_db = CreateDb('intelligent_event')

        ks = {
            'tb_name': 'kind_map',
            'field': ['id', 'name']
        }
        self.kind_map = self.ie_db.search(**ks)


@singleton_only
class Child(Father):
    def aa(self):
        print self.kind_map