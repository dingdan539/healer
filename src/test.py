# -*- coding:utf-8 -*-

import sys
import pprint
from config import *
import function.basic as fb

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(ROOT_PATH)
    from src.common.db import op
    from src.common.rabbitmq import publisher

    a = publisher.Publisher('aa_test_queue')
    a.send('dingdan')
    # db = op.CreateDb('healer')
    # a = {
    #     'tb_name': 'log'
    # }
    # mms = db.search(**a)
    # print mms
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