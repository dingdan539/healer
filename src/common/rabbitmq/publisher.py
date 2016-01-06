# -*- coding:utf-8 -*-
import pika
from .father import InitMq


class Publisher(InitMq):
    def __init__(self, queue_name):
        super(Publisher, self).__init__(queue_name)
        self._channel.queue_declare(queue=queue_name, durable=True, arguments={'delivery_mode': 1})

    def send(self, msg):
        return self._channel.basic_publish(exchange='', routing_key=self._queue_name, body=msg)