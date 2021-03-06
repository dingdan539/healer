# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

'''father class'''


class Father(object):
    """orm表父类，可以写固定字段等 被models.py里类继承"""
    pass


class DbSqlalchemy(object):
    __engine = None
    __session = None

    def __init__(self, **kwargs):
        prefix = kwargs['PREFIX']
        db_name = kwargs['DB_NAME']
        debug = kwargs['DEBUG']
        sqlalchemy = kwargs[prefix+'SQLALCHEMY']
        user = kwargs[prefix+'USER']
        pwd = kwargs[prefix+'PWD']
        server = kwargs[prefix+'SERVER']
        port = str(kwargs[prefix+'PORT'])

        uri = sqlalchemy + '://' + user + ':' + pwd + '@' + server + ':' + port + '/' + db_name + '?charset=utf8'
        self.__engine = create_engine(uri, pool_recycle=7200, echo=debug)  # pool_recycle避免超时，2小时连一次
        self.__session = scoped_session(sessionmaker(autocommit=True, bind=self.__engine))

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session