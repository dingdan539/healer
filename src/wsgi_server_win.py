# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
import wsgi

httpd = make_server('127.0.0.1', 81, wsgi.app)
print "Serving HTTP on port 81..."

httpd.serve_forever()