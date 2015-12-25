# -*- coding:utf-8 -*-
import copy

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

        self.__container.set_shield(ShieldAll())

    def analyse(self, warning_dict):
        copy_warning_dict = copy.copy(warning_dict)
        copy_warning_dict['source_id'] = 1
        res = self.__container.separate_perform(copy_warning_dict)
        res = self.__container.shield_perform(res)
        #return res