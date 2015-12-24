# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
import re


class SeparateZabbixIpStatus(Father, InterfaceSeparate):
    def separate(self, warning_dict):
        desc = warning_dict['description']
        res = re.search(r"([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})(.*?):", desc)
        ip, status = (res.group(1), res.group(2)) if res else ('', '')
        warning_dict['ip'] = ip
        warning_dict['status'] = status
        return warning_dict


class SeparateSitePool(Father, InterfaceSeparate):
    """
        this class must behind the SeparateZabbixIpStatus !
    """
    def separate(self, warning_dict):
        warning_dict['77'] = 22
        return warning_dict