# -*- coding:utf-8 -*-

from config import *
import function.basic as fb

if __name__ == "__main__":

    config = load_config_auto()

    print 'good'
    print config.ENV
    print fb.get_name()