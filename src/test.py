# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from common.db.op import *

#DbOp('dd')

# import function.decorator as fd
# import time
#
#
# @fd.run_time
# def test():
#     for i in xrange(3):
#         print i
#         time.sleep(1)
#
# test()
# engine = create_engine('mysql+mysqldb://root:@localhost:3306/cost')
# metadata = MetaData(engine)
# users_table = Table('users', metadata, Column('id', Integer, primary_key=True),
#     Column('name', String(40)),
#     Column('email', String(120)))
# users_table.create()