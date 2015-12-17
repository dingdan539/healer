# -*- coding: utf-8 -*-
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy import Column, Index
from sqlalchemy import Integer, Float, String, DateTime, Boolean, Text
from ...common.db import father

Base = declarative_base()

# ----------------------------------healer-------------------------------------------


class Healer(Base):
    __abstract__ = True


class Log(Healer, father.Father):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    message = Column(String(255), nullable=False)


class Apple(Healer, father.Father):
    __tablename__ = 'apple'
    id = Column(Integer, primary_key=True)
    wtf = Column(String(255), nullable=False)
    ddtime = Column(DateTime, default=lambda: datetime.now(), nullable=False)

# ----------------------------------asset-------------------------------------------


class Asset(DeferredReflection, Base):
    __abstract__ = True


class Server(Asset, father.Father):
    __tablename__ = 'server'
