# -*- coding:utf-8 -*-


import pika
from ...function.decorator import *


@singleton
class Q(object):
    __connection = None
    __channel = None

    def __init__(self, tag, **kwargs):
        credentials = pika.PlainCredentials('opsdev', 'opsdev')
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters('10.4.1.226', 5672, '/', credentials))
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue='aa_test')

    def send(self, msg):
        print self.__channel.basic_publish(exchange='', routing_key='aa_test', body=msg)