import pika
from ...config import load_config_auto
from ...function import basic as fb
from ...config.q.qmaps import qmaps


# class InitMq(object):
#     _connection = None
#     _channel = None
#     _queue_name = None
#
#     def __init__(self, queue_name):
#         self._queue_name = queue_name
#         prefix = qmaps[queue_name]['prefix']
#         cfg = load_config_auto()
#         qargs = fb.get_profix_property(cfg, prefix)
#         host = qargs[prefix+'HOST']
#         port = qargs[prefix+'PORT']
#         user = qargs[prefix+'USER']
#         pwd = qargs[prefix+'PWD']
#         vhost = qargs[prefix+'VHOST']
#
#         credentials = pika.PlainCredentials(user, pwd)
#         self._connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, vhost, credentials))
#         self._channel = self._connection.channel()

import rabbitpy


class InitMq(object):
    _connection = None
    _channel = None
    _queue_name = None

    def __init__(self, queue_name):
        self._queue_name = queue_name
        prefix = qmaps[queue_name]['prefix']
        cfg = load_config_auto()
        qargs = fb.get_profix_property(cfg, prefix)
        host = qargs[prefix+'HOST']
        port = qargs[prefix+'PORT']
        user = qargs[prefix+'USER']
        pwd = qargs[prefix+'PWD']
        vhost = qargs[prefix+'VHOST']

        try:
            conn = rabbitpy.Connection('amqp://%s:%s@%s:%s/%s' % (user, pwd, host, port, vhost))
            self._connection = conn
        except rabbitpy.exceptions.AMQPException:
            print 'connection-rabbitpy.exceptions.AMQPException'
        except rabbitpy.exceptions.ConnectionException:
            print 'connection-rabbitpy.exceptions.ConnectionException'
        except rabbitpy.exceptions.ConnectionResetException:
            print 'connection-rabbitpy.exceptions.ConnectionResetException'
        except rabbitpy.exceptions.RemoteClosedException:
            print 'connection-rabbitpy.exceptions.RemoteClosedException'

        try:
            chan = self._connection.channel()
            self._channel = chan
        except rabbitpy.exceptions.AMQPException:
            print 'channel-rabbitpy.exceptions.AMQPException'