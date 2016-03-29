# -*- coding:utf-8 -*-
import falcon
import json
import time
import function.basic as fb
from father import Father
from function.class_method import create


class ShieldApi(Father):
    """master have the api_path"""
    api_path = "/api/shield"
    error_msg = ''  # 提供给AuthMiddleware做判断，如果不为空，说明有错误，日志记录要记录进去

    def on_post(self, req, resp):
        params = req.params
        pool_id = params.get('pool_id', 0)
        ip = params.get('ip', '')
        key = params.get('key', '')
        source_id = params.get('source_id', 0)
        start_time = params.get('start_time', 0)
        duration = params.get('duration', 0)
        end_time = 0
        if start_time:
            if not fb.is_valid_date(start_time):
                self.error_msg = "valid_date failed. PLS use this format:2015-12-23 23:11:01"
                raise falcon.HTTPBadRequest("error", self.error_msg, code=0)
            else:
                start_time = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S')))
        else:
            c = int(time.time())
            x = time.localtime(c)
            a = time.strftime('%Y-%m-%d %H:%M:00', x)
            start_time = int(time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S')))
        end_time = start_time + (duration if duration else 3600)

        shield_module = create('shield')
        res = shield_module.insert_shield(pool_id, ip, key, source_id, start_time, end_time)
        if res.id:
            resp.body = super(ShieldApi, self).format_out(1)
        else:
            resp.body = super(ShieldApi, self).format_out(0)
        resp.status = falcon.HTTP_OK



