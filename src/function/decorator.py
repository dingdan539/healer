# -*- coding:utf-8 -*-
import time
import threading


def singleton(cls):
    instances = {}
    threadlock = threading.Lock()

    def _singleton(tag, *args, **kwargs):
        threadlock.acquire()
        if tag not in instances:
            instances[tag] = cls(tag, *args, **kwargs)
        else:
            pass
        threadlock.release()
        return instances[tag]
    return _singleton


def singleton_only(cls):
    instances = {}
    threadlock = threading.Lock()

    def _singleton_only(*args, **kwargs):
        threadlock.acquire()
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        else:
            pass
        threadlock.release()
        return instances[cls]
    return _singleton_only


def run_time(func):
    """记录函数运行时间"""
    def wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        start_time = time.time()
        myfun = func(*args, **kwargs)
        print "@%.3fs" % (time.time() - start_time)
        return myfun
    return wrapper