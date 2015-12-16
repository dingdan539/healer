# -*- coding:utf-8 -*-


def get_profix_property(cls, prefix=''):
    """返回实例自有属性包含所给前缀的一个dict"""
    dicts = cls.__dict__
    return {k: v for k, v in dicts.iteritems() if k.startswith(prefix)}


def key_in_argvs(key):
    pass