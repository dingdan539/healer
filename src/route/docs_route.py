# -*- coding:utf-8 -*-
import falcon
import os

doc_path = os.path.abspath('..') + '/docs'


class Default(object):
    no_auth = True  # 如果为True 不验证token


class Docs(Default):
    """Docs index"""
    path = "/docs"

    def on_get(self, req, resp):
        resp.content_type = "text/html"
        index = doc_path + '/build/html/index.html'
        with open(index, 'r') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK


class DocsHtml(Default):
    """Docs index"""
    path = "/{filename}"

    def on_get(self, req, resp, filename):
        resp.content_type = "text/html"
        summary = doc_path + '/build/html/' + filename
        with open(summary, 'r') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK


class DocsResource(Default):
    """Docs css """
    path = "/_static/{filename}"

    def on_get(self, req, resp, filename):
        if filename.endswith("js"):
            resp.content_type = "text/js"
        elif filename.endswith("css"):
            resp.content_type = "text/css"

        with open(doc_path + "/build/html/_static/" + filename, 'r') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK


class DocsFont(Default):
    """Docs css """
    path = "/_static/fonts/{filename}"
    def on_get(self, req, resp, filename):
        resp.content_type = "application/octet-stream"
        with open(doc_path + "/build/html/_static/fonts/" + filename, 'rb') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK


class DocsCss(Default):
    """Docs css """
    path = "/_static/css/{filename}"

    def on_get(self, req, resp, filename):
        resp.content_type = "text/css"
        with open(doc_path + "/build/html/_static/css/" + filename, 'r') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK


class DocsJs(Default):
    """Docs js """
    path = "/_static/js/{filename}"

    def on_get(self, req, resp, filename):
        resp.content_type = "text/javascript"
        with open(doc_path + "/build/html/_static/js/" + filename, 'r') as f:
            resp.body = f.read()
        resp.status = falcon.HTTP_OK