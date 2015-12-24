# -*- coding:utf-8 -*-


class ModuleFather(object):
    # father 单例
    __instance = {}
    # 标记是否已经初始化，初始化了就不要再执行init了
    # __init_tag = False

    def __new__(cls, *args, **kargs):
        if cls not in ModuleFather.__instance:
            new_cls = object.__new__(cls, *args, **kargs)
            ModuleFather.__instance[cls] = new_cls
        return ModuleFather.__instance[cls]