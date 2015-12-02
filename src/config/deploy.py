class Config(object):
    AUTHOR = "dingdan"
    ENV = "deploy"
    DEBUG = False


class DeployConfig(Config):
    DB_SQLALCHEMY = 'mysql+mysqldb'
    DB_USER = 'root'
    DB_PWD = ''
    DB_SERVER = 'localhost'
    DB_PORT = '3306'