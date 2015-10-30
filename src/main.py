# -*- coding:utf-8 -*-
#from flask import Flask
from config import load_config_auto
import function.basic as fb

if __name__ == "__main__":
    #app = Flask(__name__)
    config = load_config_auto()
    #app.config.from_object(config)

    print config.ENV
    print fb.get_name()