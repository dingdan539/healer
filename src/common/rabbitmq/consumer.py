# -*- coding:utf-8 -*-
from .father import InitMq


# class Consumer(InitMq):
#     def __init__(self, queue_name):
#         super(Consumer, self).__init__(queue_name)
#         self._channel.queue_declare(queue=queue_name, durable=True)
#
#     def receive(self, fun):
#         def my_fun(channel, method, properties, body):
#             fun(body)
#         self._channel.basic_consume(my_fun, queue=self._queue_name, no_ack=True)
#         self._channel.start_consuming()

import rabbitpy


class Consumer(InitMq):
    queue = None

    def __init__(self, queue_name):
        super(Consumer, self).__init__(queue_name)
        queue = rabbitpy.Queue(self._channel, queue_name)
        queue.durable = True
        queue.declare()
        self.queue = queue

    def receive(self, fun):
        for message in self.queue:
            fun(message)