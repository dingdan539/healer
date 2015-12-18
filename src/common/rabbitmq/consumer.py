# -*- coding:utf-8 -*-
from .father import InitMq


class Consumer(InitMq):
    def __init__(self, queue_name):
        super(Consumer, self).__init__(queue_name)
        self._channel.queue_declare(queue=queue_name, durable=True)

    def receive(self, fun):
        self._channel.basic_consume(fun, queue=self._queue_name, no_ack=True)
        print "alery in "
        self._channel.start_consuming()
