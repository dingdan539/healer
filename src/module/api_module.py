# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather
from ..function.decorator import *


@singleton_only
class ApiModule(ModuleFather):
    __db = None

    def __init__(self):
        """父类__new__已实现单例，__init__每次都会调用，需要self.x判断是否已创建"""
        if not self.__db:
            self.__db = op.CreateDb('intelligent_event')

    def insert_api_log(self, from_ip, path, user_id, date, remark):
        kwargs = {
            'tb_name': 'api_log',
            'field': {'from_ip': from_ip, 'path': path, 'user_id': user_id, 'date': date, 'remark': remark}
        }
        data = self.__db.insert(**kwargs)
        return data
