import pika
from ...config import load_config_auto
from ...function import basic as fb
from ...config.q.qmaps import qmaps


class InitMq(object):
    __connection = None
    __channel = None

    def __init__(self, queue_name):
        prefix = qmaps[queue_name]['prefix']
        cfg = load_config_auto()
        qargs = fb.get_profix_property(cfg, prefix)
        host = qargs[prefix+'HOST']
        port = qargs[prefix+'PORT']
        user = qargs[prefix+'USER']
        pwd = qargs[prefix+'PWD']
        vhost = qargs[prefix+'VHOST']

        credentials = pika.PlainCredentials(user, pwd)
        self.__connection = pika.BlockingConnection(pika.ConnectionParameters(host, port, vhost, credentials))
        self.__channel = self.__connection.channel()