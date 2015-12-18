# -*- coding:utf-8 -*-
from .father import InitMq


class Consumer(InitMq):
    def __init__(self, queue_name, cb_fun):
        super(Consumer, self).__init__(queue_name)
        self._channel.queue_declare(queue=queue_name, durable=True)
        Consumer.callback = cb_fun
        Consumer.callback('123')

    @staticmethod
    def callback(self, msg):
        print msg

    @staticmethod
    def __callback(ch, method, properties, body):
        print body
        Consumer.callback(body)

    def gogo(self):
        pass

    def receive(self):
        self._channel.basic_consume(self.__callback, queue=self._queue_name, no_ack=True)
        self._channel.start_consuming()
