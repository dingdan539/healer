# -*- coding:utf-8 -*-
import falcon
import json
from father import Father


class AlertApi(Father):
    """master have the api_path"""
    api_path = ""
    error_msg = ""  # 提供给AuthMiddleware做判断，如果不为空，说明有错误，日志记录要记录进去

    def on_get(self, req, resp):
        resp.body = "i wanna f u"
        resp.status = falcon.HTTP_OK