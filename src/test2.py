# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(ROOT_PATH)
    from src.common.db import op
    from src.common.rabbitmq import consumer

    def call_back(aa, bb, cc, msg):
        print msg + '-qusi'

    a = consumer.Consumer('aa_test_queue')
    a.receive(call_back)
    # db = op.CreateDb('asset')
    # #db.init_table()
    # a = {
    #     'tb_name': 'server',
    #     'where': {
    #         'ip =': '10.4.1.155'
    #     }
    # }
    # print db.search(**a)

    # a = {
    #     'tb_name': 'cao',
    #     'field': ['caonima', 'name', 'id'],
    #     'or': {
    #     },
    #     'order': {
    #         'id': 'desc'
    #     },
    #     'limit': [1, 2]
    # }
    # mms = db.search(**a)

    # b = {
    #     'tb_name': 'cao',
    #     'field': {
    #         'name': 'e4',
    #         'caonima': 'e4'
    #     },
    #     'where': {
    #         'name like': 'z%'
    #     }
    # }
    # mms = db.insert(**b)
    # print mms
    #pprint.pprint(db.search())
    #
    # config = load_config_auto()
    #
    #
    # from src.common.db.op import DbOp
    #
    # dbargs = fb.get_profix_property(config, 'DB')
    # dbargs['DEBUG'] = config.DEBUG
    #
    # db_res = DbOp('haohao', **dbargs)