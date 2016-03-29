class Config(object):
    AUTHOR = "dingdan"
    ENV = "devel"
    DEBUG = False


class DevelConfig(Config):
    DOMAIN_PROFIX = ''

    DB_SQLALCHEMY = 'mysql+mysqldb'
    DB_USER = 'root'
    DB_PWD = ''
    DB_SERVER = 'localhost'
    DB_PORT = '3306'

    RMQ_HOST = '10.4.1.226'
    RMQ_PORT = 5672
    RMQ_USER = 'opsdev'
    RMQ_PWD = 'opsdev'
    RMQ_VHOST = '/'

    REDIS_HOST = 'redis01.oms.yihaodian.com.cn'
    REDIS_PORT = 6379