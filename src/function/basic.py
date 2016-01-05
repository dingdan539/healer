# -*- coding:utf-8 -*-
import subprocess


def get_profix_property(cls, prefix=''):
    """返回实例自有属性包含所给前缀的一个dict"""
    dicts = cls.__dict__
    return {k: v for k, v in dicts.iteritems() if k.startswith(prefix)}


def command(cmdstr):
    proc = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    code = proc.returncode
    return code, stdout, stderr