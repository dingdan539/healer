# -*- coding:utf-8 -*-


class InterfaceShield(object):
    """
        屏蔽策略
    """
    def shield(self, warning_dict):
        pass


class InterfaceSeparate(object):
    """
        切分策略
    """
    def separate(self, warning_dict):
        pass


class InterfaceOutPut(object):
    """
        输出策略
    """
    def output(self, warning_dict):
        pass


class InterfaceProcess(object):
    """
        分析策略
    """
    def process(self, warning_dict):
        pass