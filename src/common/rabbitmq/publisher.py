# -*- coding:utf-8 -*-
import pika
from .father import InitMq


# class Publisher(InitMq):
#     def __init__(self, queue_name):
#         super(Publisher, self).__init__(queue_name)
#         self._channel.queue_declare(queue=queue_name, durable=True)  # , arguments={'delivery_mode': 2} 持久化
#
#     def send(self, msg):
#         return self._channel.basic_publish(exchange='', routing_key=self._queue_name, body=msg)

import rabbitpy


class Publisher(InitMq):
    queue = None

    def __init__(self, queue_name):
        super(Publisher, self).__init__(queue_name)
        queue = rabbitpy.Queue(self._channel, queue_name)
        queue.durable = True
        queue.declare()
        self.queue = queue
        self._channel.enable_publisher_confirms()

    def send(self, msg):
        message = rabbitpy.Message(self._channel, msg)
        res = message.publish('', self._queue_name)
