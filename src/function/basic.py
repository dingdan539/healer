# -*- coding:utf-8 -*-
import subprocess
import os
import time


def get_profix_property(cls, prefix=''):
    """返回实例自有属性包含所给前缀的一个dict"""
    dicts = cls.__dict__
    return {k: v for k, v in dicts.iteritems() if k.startswith(prefix)}


def get_files(path, last_prefix=''):
    """返回一个路径下的所有文件名，如果last_prefix不为空，则只取出符合的后缀名"""
    tmp = []
    for p in os.listdir(path):
        if last_prefix:
            if p.endswith(last_prefix):
                tmp.append(p)
        else:
            tmp.append(p)
    return tmp


def command(cmdstr):
    proc = subprocess.Popen(cmdstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    code = proc.returncode
    return code, stdout, stderr


def is_valid_date(date):
    """判断是否是一个有效的日期字符串"""
    try:
        time.strptime(date, "%Y-%m-%d %H:%M:%S")
        return True
    except Exception as e:
        return False