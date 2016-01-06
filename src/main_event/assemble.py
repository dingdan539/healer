# -*- coding:utf-8 -*-
import copy

from ..function.decorator import *
from ..main_event.container import *
from pattern_shield import *
from pattern_separate import *
from pattern_output import *
from pattern_process import *


@singleton_only
class ZabbixAnalyse(object):
    __container = None

    def __init__(self):
        self.__container = Container()
        self.__container.set_separate(SeparateZabbixIpStatus())
        self.__container.set_separate(SeparateSitePool())
        self.__container.set_separate(SeparateType())

        self.__container.set_shield(ShieldAll())

        self.__container.set_output(OutputZabbix())
        self.__container.set_output(OutputMqStability())  # 稳定性报警就退到这个队列里

        self.__container.set_process(ProcessZabbixTomcat())

    def analyse(self, warning_dict):
        copy_warning_dict = copy.copy(warning_dict)
        data = self.__container.separate_perform(copy_warning_dict)
        result = self.__container.shield_perform(data)
        if result:
            self.__container.output_perform(data)
            self.__container.process_perform(data)