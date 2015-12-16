class Config(object):
    AUTHOR = "dingdan"
    ENV = "deploy"
    DEBUG = False


class DeployConfig(Config):
    DB_SQLALCHEMY = 'mysql+mysqldb'
    DB_USER = 'opsdev'
    DB_PWD = 'opsdev_1haodian'
    DB_SERVER = 'masterdb.oms.yihaodian.com.cn'
    DB_PORT = '3306'