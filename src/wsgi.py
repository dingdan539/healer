# -*- coding:utf-8 -*-
import os
import sys
import copy
import falcon
import route.docs_route as r_docs
from config import *
from api.middleware import AuthMiddleware
import function.basic as fb

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_PATH)


class Wsgi(object):
    app = falcon.API(middleware=[AuthMiddleware()])
    root_path = os.getcwd()
    root_child_path = '/api'
    root_api_path = os.getcwd() + root_child_path
    api_files = []

    def __init__(self):
        self.api_files = fb.get_files(self.root_api_path, '_api.py')

    def process(self):
        """api文件夹下的api初始化"""
        if self.api_files:
            config = load_config_auto()
            profix = config.DOMAIN_PROFIX
            for f in self.api_files:
                f = f.split('.')[0]
                m_path = "api."+f

                m = __import__(m_path, {}, {}, ['not None'])
                f = f.split('_')
                f_c = len(f)
                f_name = ''
                if f_c > 1:
                    for i in range(0, f_c, 1):
                        f_name += f[i].capitalize()
                else:
                    f_name = f_c[0].capitalize()

                obj = getattr(m, f_name)()
                self.app.add_route(profix + obj.api_path, obj)

        def my_serializer(req, exception):
            """修改error的默认content-type类型"""
            exception = exception.to_json()
            return "application/json", exception
        self.app.set_error_serializer(my_serializer)
        """
            添加others路径
        """
        for i in [r_docs.Docs(), r_docs.DocsHtml(), r_docs.DocsResource(),
                  r_docs.DocsJs(), r_docs.DocsCss(), r_docs.DocsFont()]:
            self.app.add_route(profix + i.path, i)

    def get_app(self):
        self.process()
        return self.app

o = Wsgi()
app = o.get_app()