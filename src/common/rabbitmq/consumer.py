# -*- coding:utf-8 -*-
import pika


class Consumer(object):
    __connection = None
    __channel = None

    def __init__(self, **kwargs):
        credentials = pika.PlainCredentials('opsdev', 'opsdev')
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters('10.4.1.226', 5672, '/', credentials))
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue='aa_test')

    def get(self):
        self.__channel.basic_consume(self.callback, queue='aa_test', no_ack=True)

        print ' [*] Waiting for messages. To exit press CTRL+C'
        self.__channel.start_consuming()

    @staticmethod
    def callback(self, ch, method, properties, body):
        print " [x] Received %r" % (body,)

