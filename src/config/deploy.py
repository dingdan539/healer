class Config(object):
    AUTHOR = "dingdan"
    ENV = "deploy"
    DEBUG = False


class DeployConfig(Config):
    ENV = "deploy"
    DEBUG = False