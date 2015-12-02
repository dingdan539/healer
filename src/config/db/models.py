# -*- coding: utf-8 -*-
from sqlalchemy import Column, Index
from sqlalchemy import Integer, Float, String, DateTime, Boolean, Text
from ...common.db import father


class Log(father.Base, father.Father):
    __tablename__ = 'log'
    id = Column(Integer(11), primary_key=True)
    message = Column(String(255))