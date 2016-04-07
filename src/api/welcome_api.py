# -*- coding:utf-8 -*-
import falcon
import json
import os
from father import Father


class WelcomeApi(Father):
    """master have the api_path"""
    api_path = "/hc"
    error_msg = ""  # 提供给AuthMiddleware做判断，如果不为空，说明有错误，日志记录要记录进去
    no_auth = True

    def on_get(self, req, resp):
        resp.body = 'ok'
        resp.status = falcon.HTTP_OK