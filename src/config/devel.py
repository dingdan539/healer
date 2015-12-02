class Config(object):
    AUTHOR = "dingdan"
    ENV = "devel"
    DEBUG = True


class DevelConfig(Config):
    DB_SQLALCHEMY = 'mysql+mysqldb'
    DB_USER = 'root'
    DB_PWD = ''
    DB_SERVER = 'localhost'
    DB_PORT = '3306'