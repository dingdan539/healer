# -*- coding:utf-8 -*-
import falcon
import json
import time
from father import Father
from function.class_method import create


class AlertApi(Father):
    """Docstring for class Foo."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    api_path = "/api/alert"
    error_msg = ''  #: 提供给AuthMiddleware做判断，如果不为空，说明有错误，日志记录要记录进去

    def on_post(self, req, resp):
        params = req.params
        ip = params.get('ip', '')
        site_id = params.get('site_id', 0)
        pool_id = params.get('pool_id', 0)
        description = params.get('description', '')
        clock = int(time.time())
        kind_id = 1
        level_id = params.get('level_id', 4)  # 4是应用层
        source_id = params.get('source_id', 0)

        if ip:
            server_module = create('server')
            pool_id = server_module.search_poolid_by_ip(ip)
            site_id = server_module.search_siteid_by_poolid(pool_id)
        try:
            description = json.loads(description)
            event_module = create('event')
            res = event_module.insert_event(ip, site_id, pool_id, description, clock, kind_id, level_id, source_id)
            if res.id:
                resp.body = super(AlertApi, self).format_out(1)
            else:
                resp.body = super(AlertApi, self).format_out(0)
            resp.status = falcon.HTTP_OK
        except Exception as e:
            self.error_msg = "%s" % e
            raise falcon.HTTPBadRequest("error", self.error_msg, code=0)

        # description = params.get('description', '')
        # clock = params.get('clock', int(time.time()))
        # source_id = params.get('source_id', '')
        # json_doc = params.get('json_doc', '')
        # json_doc = json.loads(json_doc)
        # print json_doc
        # source = json_doc.get('source', '')

        #resp.status = falcon.HTTP_200  # This is the default status
