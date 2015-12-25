# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
from ..function.class_method import create


class ShieldAll(Father, InterfaceShield):
    """
        this class must behind the pattern_separate
    """
    def __init__(self):
        super(ShieldAll, self).__init__()

    def shield(self, warning_dict):
        desc = warning_dict['description']
        clock = warning_dict['clock']
        ip = warning_dict['ip']
        pool_id = warning_dict['pool_id']
        source_id = warning_dict['source_id']

        kwargs = {
            'tb_name': 'shield',
            'where': {
                'start_time >=': clock,
                'end_time <=': clock,
            },
            'or': {
                'pool_id =': 486,
                'ip =': 2
            }
        }
        print self.f_kind_map
        print super(ShieldAll, self).f_kind_map
        #exit(0)
        #print father.f_ie_db.search(**kwargs)
