# -*- coding:utf-8 -*-
from ..function.decorator import *
from ..main_event.container import *
from pattern_shield import *
from pattern_separate import *


@singleton_only
class ZabbixAnalyse(object):
    __container = None

    def __init__(self):
        self.__container = Container()
        self.__container.set_separate(SeparateZabbixIpStatus())
        self.__container.set_separate(SeparateSitePool())

    def analyse(self, warning_dict):
        res = self.__container.separate_perform(warning_dict)
        print res