# -*- coding:utf-8 -*-
import pika
from ...config import load_config_auto
from ...config.q.qmaps import qmaps


class Publisher(object):
    __connection = None
    __channel = None

    def __init__(self, queue_name):
        cfg = load_config_auto()
        self.dbargs = fb.get_profix_property(cfg, self.prefix)
        
        credentials = pika.PlainCredentials('opsdev', 'opsdev')
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters('10.4.1.226', 5672, '/', credentials))
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue='aa_test')

    def send(self, msg):
        print self.__channel.basic_publish(exchange='', routing_key='aa_test', body=msg)