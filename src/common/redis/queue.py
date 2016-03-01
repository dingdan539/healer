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
        redis_kwargs = {host: host, port: port}
        try:
            self._connection = redis.Redis(**redis_kwargs)
        except Exception, e:
            print Exception, e

    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self._key, timeout=timeout)
        else:
            item = self.__db.lpop(self._key)

        if item:
            return item
            #item = item[1]