import redis
from ...config import load_config_auto
from ...function import basic as fb
from ...config.q.qmaps import qmaps


class InitQ(object):
    _connection = None
    _key = None

    def __init__(self, key):
        self._key = key
        prefix = qmaps[key]['prefix']
        cfg = load_config_auto()
        qargs = fb.get_profix_property(cfg, prefix)
        host = qargs[prefix+'HOST']
        port = qargs[prefix+'PORT']
        db = 0

        try:
            self._connection = redis.Redis(host=host, port=port, db=db)
        except Exception, e:
            print Exception, e

    def blpop(self, fun):
        while True:
            item = self._connection.blpop(self._key, timeout=None)
            if item:
                fun(item[1])

    def rpush(self, data):
        return self._connection.rpush(self._key, data)
