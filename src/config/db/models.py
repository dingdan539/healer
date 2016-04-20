# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy import Column, Index
from sqlalchemy import Integer, Float, String, DateTime, Boolean, Text
from ...common.db import father

Base = declarative_base()

# ----------------------------------Intelligent_event-------------------------------------------


class Intelligent_event(DeferredReflection, Base):
    __abstract__ = True

class Alert_2016(Intelligent_event, father.Father):
    __tablename__ = 'alert_2016'

class Alert_2017(Intelligent_event, father.Father):
    __tablename__ = 'alert_2017'

class Alert_2018(Intelligent_event, father.Father):
    __tablename__ = 'alert_2018'

class Alert_2019(Intelligent_event, father.Father):
    __tablename__ = 'alert_2019'

class Alert_2020(Intelligent_event, father.Father):
    __tablename__ = 'alert_2020'

class Api_log(Intelligent_event, father.Father):
    __tablename__ = 'api_log'

class Important_event(Intelligent_event, father.Father):
    __tablename__ = 'important_event'

class Kind_map(Intelligent_event, father.Father):
    __tablename__ = 'kind_map'

class Level_map(Intelligent_event, father.Father):
    __tablename__ = 'level_map'

class Shield(Intelligent_event, father.Father):
    __tablename__ = 'shield'

class Source_map(Intelligent_event, father.Father):
    __tablename__ = 'source_map'

class Type_map(Intelligent_event, father.Father):
    __tablename__ = 'type_map'

class User_token(Intelligent_event, father.Father):
    __tablename__ = 'user_token'

# ----------------------------------Asset-------------------------------------------


class Asset(DeferredReflection, Base):
    __abstract__ = True


class Server(Asset, father.Father):
    __tablename__ = 'server'


class App(Asset, father.Father):
    __tablename__ = 'app'


class Site(Asset, father.Father):
    __tablename__ = 'site'

class Switch_server(Asset, father.Father):
    __tablename__ = 'switch_server'
