# -*- coding:utf-8 -*-
from src.common.db import op
from ..public.module_father import ModuleFather


class ServerModule(ModuleFather):
    __db = None

    def __init__(self):
        if not self.__db:
            self.__db = op.CreateDb('asset')

    def search_poolid_by_ip(self, ip):
        if not ip:
            return 0
        kwargs = {
            'tb_name': 'server',
            'field': ['app_id'],
            'where': {
                'ip =': ip
            }
        }

        data = self.__db.search(**kwargs)['data']
        return data[0]['app_id'] if data else 0

    def search_siteid_by_poolid(self, pool_id):
        if not pool_id:
            return 0
        kwargs = {
            'tb_name': 'app',
            'field': ['site_id'],
            'where': {
                'id =': pool_id
            }
        }

        data = self.__db.search(**kwargs)['data']
        return data[0]['site_id'] if data else 0

