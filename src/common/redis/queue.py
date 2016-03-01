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
        redis_kwargs = {host: host, port: port, db: db}
        try:
            self._connection = redis.Redis(**redis_kwargs)
            print 11111111111111
            print self._connection
        except Exception, e:
            print Exception, e

    def get(self, block=True, timeout=None):
        if block:
            item = self._connection.blpop(self._key, timeout=timeout)
        else:
            item = self._connection.lpop(self._key)

        if item:
            return item
            #item = item[1]