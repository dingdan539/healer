# -*- coding:utf-8 -*-
from ...function.decorator import *
from father import *
from ...function import basic as fb
from ...config.db.databases import dbmaps
from ...config import load_config_auto
from sqlalchemy import Table
from ...config.db import models

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
        self.dbargs['DB_NAME'] = db_name
        self.dbargs['DEBUG'] = cfg.DEBUG


class CreateDb(InitCreateDb):
    __db_name = None
    __instance = None
    __engine = None
    __session = None

    def __init__(self, db_name):
        super(CreateDb, self).__init__(db_name)
        self.__db_name = db_name
        self.__instance = DbOp(db_name, **self.dbargs)
        self.__engine = self.__instance.get_engine()
        self.__session = self.__instance.get_session()

    def init_table(self):
        Base.metadata.create_all(bind=self.__engine)

    def execute(self, sql):
        try:
            prefix = sql[:sql.index(' ')].lower()
            res = self.__session.execute(sql)
            if prefix == 'select':
                return res.fetchall()
            elif prefix in ['update', 'delete']:
                return res.rowcount
            elif prefix == 'insert':
                return 'insert go'
            else:
                return False
        except Exception, data:
            print 'mymy'
            print data
            print type(data)

    def __default_args(self, **kwargs):
        canshu = dict()
        canshu['tb_name'] = kwargs.get('tb_name', '')
        canshu['field'] = kwargs.get('field', [])
        canshu['where'] = kwargs.get('where', {})
        canshu['or'] = kwargs.get('or', {})
        canshu['in'] = kwargs.get('in', {})
        canshu['order'] = kwargs.get('order', {})
        canshu['limit'] = kwargs.get('limit', [])
        return canshu

    def search(self, **kwargs):
        canshu = self.__default_args(**kwargs)
        if dbmaps[self.__db_name]['tables']
        #users_table = Table('log', Base.metadata, autoload_with=self.__engine)
        result = self.__session.query(models.Log.message).filter_by(message='qusi2').all()
        return result