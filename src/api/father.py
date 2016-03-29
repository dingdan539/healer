# -*- coding:utf-8 -*-
import json


class Father(object):
    @staticmethod
    def format_out(code=1, title='', description=''):
        if code == 1:
            title = 'succ'
            description = 'success'
        else:
            title = 'fail'
            description = 'failed'
        return json.dumps({'code': code, 'title': title, 'description': description})