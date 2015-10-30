class Config(object):
    AUTHOR = "dingdan"
    ENV = "devel"
    DEBUG = True


class DeployConfig(Config):
    ENV = "deploy"
    DEBUG = False


class DevelConfig(Config):
    ENV = "devel"
    DEBUG = True