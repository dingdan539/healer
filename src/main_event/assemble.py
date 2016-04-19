# -*- coding:utf-8 -*-
import copy

from ..function.decorator import *
from ..main_event.container import *
from pattern_shield import *
from pattern_separate import *
from pattern_output import *
from pattern_process import *
from pattern_stability_process import *


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
        self.__container.set_output(OutputZabbixMqStability())  # 稳定性报警就推到这个队列里

        # 以下只会分析可用性报警
        self.__container.set_process(ProcessZabbixFilter())
        self.__container.set_process(ProcessZabbixStandard())
        self.__container.set_process(ProcessDirect())

    def analyse(self, warning_dict):
        copy_warning_dict = copy.copy(warning_dict)
        #print copy_warning_dict
        data = self.__container.separate_perform(copy_warning_dict)
        result = self.__container.shield_perform(data)
        #print data
        #print result
        if result:
            self.__container.output_perform(data)
            self.__container.process_perform(data)


@singleton_only
class ZabbixStabilityAnalyse(object):
    __container = None
    __threadpool = None

    def __init__(self):
        self.__container = Container()

        init = ProcessZabbixStability()

        th = threading.Thread(target=init.scan_count)
        self.__threadpool = th
        th.start()

        self.__container.set_process(init)

    def analyse(self, warning_dict):
        copy_warning_dict = copy.copy(warning_dict)

        self.__container.process_perform(copy_warning_dict)