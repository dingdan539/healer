# -*- coding:utf-8 -*-
from ...function.decorator import *
from father import *
from ...function import basic as fb
from ...config.db.databases import dbmaps
from ...config import load_config_auto

@singleton
class DbOp(object):
    __instance = None

    def __init__(self, tag, **kwargs):
        self.__instance = DbSqlalchemy(**kwargs)

    def get_engine(self):
        return self.__instance.engine

    def get_session(self):
        return self.__instance.session


class InitCreateDb(object):
    def __init__(self, db_name):
        prefix = dbmaps[db_name]['prefix']
        cfg = load_config_auto()
        self.dbargs = fb.get_profix_property(cfg, prefix)
        self.dbargs['DEBUG'] = cfg.DEBUG


class CreateDb(InitCreateDb):
    __instance = None

    def __init__(self, db_name):
        super(CreateDb, self).__init__(db_name)
        self.__instance = DbOp(db_name, **self.dbargs)

    def search(self):
        print self.__instance
