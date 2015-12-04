# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

'''father class'''


class Father(object):
    """orm表父类，可以写固定字段等 被models.py里类继承"""
    pass


class DbSqlalchemy(object):
    __engine = None
    __session = None

    def __init__(self, **kwargs):
        db_sqlalchemy = kwargs['DB_SQLALCHEMY']
        db_user = kwargs['DB_USER']
        db_pwd = kwargs['DB_PWD']
        db_server = kwargs['DB_SERVER']
        db_port = kwargs['DB_PORT']
        db_name = kwargs['DB_NAME']
        debug = kwargs['DEBUG']

        uri = db_sqlalchemy + '://' + db_user + ':' + db_pwd + '@' + db_server + ':' + db_port + '/' \
            + db_name + '?charset=utf8'
        self.__engine = create_engine(uri, echo=debug)
        self.__session = scoped_session(sessionmaker(autocommit=True, bind=self.__engine))

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self.__session