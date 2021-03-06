# -*- coding:utf-8 -*-
from ..common.db.op import *
from ..common.redis.queue import *


class Father(object):
    # father 单例
    __instance = {}
    # 标记是否已经初始化，初始化了就不要再执行init了
    __init_tag = False

    def __new__(cls, *args, **kargs):
        if cls not in Father.__instance:
            new_cls = object.__new__(cls, *args, **kargs)
            Father.__instance[cls] = new_cls
        return Father.__instance[cls]

    f_ie_db = None  # intelligent_event db 句柄
    f_stb_p_q = None
    f_kind_map = None
    f_level_map = None
    f_source_map = None
    f_type_map = None

    def __init__(self):
        if not Father.__init_tag:
            Father.__init_tag = True
            Father.f_ie_db = CreateDb('intelligent_event')
            Father.f_stb_p_q = InitQ('zabbix_stability_queue')

            ks = {
                'tb_name': 'kind_map',
                'field': ['id', 'name']
            }
            res = Father.f_ie_db.search(**ks)
            Father.f_kind_map = {v['id']: v['name'] for v in res['data']}

            ks = {
                'tb_name': 'level_map',
                'field': ['id', 'name']
            }
            res = Father.f_ie_db.search(**ks)
            Father.f_level_map = {v['id']: v['name'] for v in res['data']}

            ks = {
                'tb_name': 'source_map',
                'field': ['id', 'name']
            }
            res = Father.f_ie_db.search(**ks)
            Father.f_source_map = {v['id']: v['name'] for v in res['data']}

            ks = {
                'tb_name': 'type_map',
                'field': ['id', 'name', 'level_id', 'kind_id']
            }
            res = Father.f_ie_db.search(**ks)
            # 字典解析
            Father.f_type_map = {
                v['id']: {'name': v['name'], 'level_id': v['level_id'], 'kind_id': v['kind_id']} for v in res['data']
            }