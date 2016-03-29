# -*- coding: utf-8 -*-
import time
import falcon
import json
import datetime
from function.class_method import create
from function.decorator import *


class AuthMiddleware(object):
    """api 权限验证 待补充"""
    _api_module = None
    _token_module = None
    _user_id = 0
    _from_ip = ''
    _path = None

    def process_request(self, req, resp):
        self._api_module = create('api')
        self._token_module = create('token')
        try:
            pass
            tmp = req.access_route
            if isinstance(tmp, list):
                if len(tmp) > 0:
                    self._from_ip = tmp[0]
        except Exception as e:
            print e

        self._path = req.path
        date = int(time.time())

        token = req.get_param('token', default='')
        token_result = self._token_module.get_token(token)
        if token_result:
            token_result = token_result['data']

        if not token_result:
            msg = "token is not found"
            self._api_module.insert_api_log(self._from_ip, self._path, 0, date, msg)
            raise falcon.HTTPBadRequest("error", msg, code=0)
        else:
            self._user_id = token_result[0].get('id', 0)

    def process_response(self, req, resp, resource):
        remark = resource.error_msg if (hasattr(resource, 'error_msg') and resource.error_msg) else json.dumps(req.params)
        date = int(time.time())
        try:
            self._api_module.insert_api_log(self._from_ip, self._path, self._user_id, date, remark)
        except Exception as e:
            msg = "%s" % e
            self._api_module.insert_api_log(self._from_ip, self._path, self._user_id, date, msg)
            raise falcon.HTTPBadRequest("error", "wrote log failed, PLS check the log", code=0)