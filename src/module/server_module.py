# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather


class ServerModule(ModuleFather):
    __db = None

    def __init__(self):
        if not self.__db:
            print 111111111111111111111111111111
            self.__db = op.CreateDb('asset')

    def search_poolid_by_ip(self, ip):
        kwargs = {
            'tb_name': 'server',
            'field': ['app_id'],
            'where': {
                'ip =': ip
            }
        }

        print self.__db.search(**kwargs)
