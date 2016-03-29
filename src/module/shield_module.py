# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather
from ..function.decorator import *


class ShieldModule(ModuleFather):
    __db = None

    def __init__(self):
        """父类__new__已实现单例，__init__每次都会调用，需要self.x判断是否已创建"""
        if not self.__db:
            self.__db = op.CreateDb('intelligent_event')

    def insert_shield(self, pool_id, ip='', key='', source_id=0, start_time=0, end_time=0):
        kwargs = {
            'tb_name': 'shield',
            'field': {'pool_id': pool_id, 'ip': ip, 'key': key,
                      'source_id': source_id, 'start_time': start_time,
                      'end_time': end_time}
        }
        data = self.__db.insert(**kwargs)
        return data
