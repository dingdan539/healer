# -*- coding:utf-8 -*-
import pika
from .father import InitMq


class Publisher(InitMq):
    def __init__(self, queue_name):
        super(Publisher, self).__init__(queue_name)
        self._channel.queue_declare(queue=queue_name, durable=True, properties=pika.BasicProperties(delivery_mode=2))

    def send(self, msg):
        print self._channel.basic_publish(exchange='', routing_key='', body=msg)