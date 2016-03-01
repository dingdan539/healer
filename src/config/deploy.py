class Config(object):
    AUTHOR = "dingdan"
    ENV = "deploy"
    DEBUG = False


class DeployConfig(Config):
    DB_SQLALCHEMY = 'mysql+mysqldb'
    DB_USER = 'opsdev'
    DB_PWD = 'opsdev_1haodian'
    DB_SERVER = 'masterdb.oms.yihaodian.com.cn'
    DB_PORT = 3306

    RMQ_HOST = '10.4.1.226'
    RMQ_PORT = 5672
    RMQ_USER = 'opsdev'
    RMQ_PWD = 'opsdev'
    RMQ_VHOST = '/'

    REDIS_HOST = 'redis01.oms.yihaodian.com.cn'
    REDIS_PORT = 6379