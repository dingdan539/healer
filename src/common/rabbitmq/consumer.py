# -*- coding:utf-8 -*-
from .father import InitMq


class Consumer(InitMq):
    queue_name = None

    def __init__(self, queue_name):
        self.queue_name = queue_name
        super(Consumer, self).__init__(queue_name)
        self.__channel.queue_declare(queue=queue_name, durable=True)

    @staticmethod
    def callback(ch, method, properties, body):
        print body

    def receive(self):
        self.__channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)
        self.__channel.start_consuming()
