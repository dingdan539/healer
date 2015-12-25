# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
from ..function.class_method import create
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
        ip = warning_dict['ip']
        server_module = create('server')
        pool_id = server_module.search_poolid_by_ip(ip)
        site_id = server_module.search_siteid_by_poolid(pool_id)
        warning_dict['pool_id'] = pool_id
        warning_dict['site_id'] = site_id
        return warning_dict


class SeparateType(Father, InterfaceSeparate):
    def separate(self, warning_dict):
        desc = warning_dict['description']