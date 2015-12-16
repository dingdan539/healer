# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Index
from sqlalchemy import Integer, Float, String, DateTime, Boolean, Text
from ...common.db import father


class Log(father.Base, father.Father):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    message = Column(String(255), nullable=False)


class Apple(father.Base, father.Father):
    __tablename__ = 'apple'
    id = Column(Integer, primary_key=True)
    wtf = Column(String(255), nullable=False)
    ddtime = Column(DateTime, default=lambda: datetime.now(), nullable=False)


class Cao(father.DeferredReflection, father.Base, father.Father):
    __tablename__ = 'cao'
