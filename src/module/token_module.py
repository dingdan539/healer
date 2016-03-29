# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather
from ..function.decorator import *
import datetime
import time
import hashlib


class TokenModule(ModuleFather):
    __db = None

    def __init__(self):
        if not self.__db:
            self.__db = op.CreateDb('intelligent_event')

    def create_token(self, user_name):
        today = datetime.date.today()
        time_stamp = time.mktime(today.timetuple())
        md = hashlib.md5()
        md.update(user_name)
        md_str = md.hexdigest()
        kwargs = {
            'tb_name': 'user_token',
            'field': {'user_name': user_name, 'token': md_str, 'get_time': time_stamp}
        }
        data = self.__db.insert(**kwargs)
        return data

    def get_token(self, token):
        if not token:
            return None
        else:
            kwargs = {
                'tb_name': 'user_token',
                'field': ['id', 'user_name', 'token', 'get_time'],
                'where': {'token =': token}
            }
            data = self.__db.search(**kwargs)
            return data

