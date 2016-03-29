# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather
from ..function.decorator import *


class EventModule(ModuleFather):
    __db = None

    def __init__(self):
        """父类__new__已实现单例，__init__每次都会调用，需要self.x判断是否已创建"""
        if not self.__db:
            self.__db = op.CreateDb('intelligent_event')

    def insert_event(self, ip, site_id, pool_id, description, clock, kind_id, level_id, source_id):
        kwargs = {
            'tb_name': 'important_event',
            'field': {'ip': ip, 'site_id': site_id, 'pool_id': pool_id,
                      'description': description, 'clock': clock, 'clock': clock,
                      'kind_id': kind_id, 'level_id': level_id, 'source_id': source_id}
        }
        data = self.__db.insert(**kwargs)
        return data
