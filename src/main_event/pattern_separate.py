# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
from ..function.class_method import create
import re


class SeparateZabbixIpStatus(Father, InterfaceSeparate):
    def separate(self, warning_dict):
        desc = warning_dict['description']
        res = re.search(r"([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})(.*?):", desc)
        try:
            ip, status = (res.group(1), res.group(2)) if res else ('', '')
        finally:
            warning_dict['ip'] = ip
            warning_dict['status'] = status


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


class SeparateType(Father, InterfaceSeparate):
    def separate(self, warning_dict):
        desc = warning_dict['description'][:80].lower()
        for i in self.f_type_map:
            res = re.search(self.f_type_map[i]['name'], desc)
            if res:
                warning_dict['type_id'] = i
                warning_dict['kind_id'] = self.f_type_map[i]['kind_id']
                warning_dict['level_id'] = self.f_type_map[i]['level_id']
                break
            else:
                warning_dict['type_id'] = 0
                warning_dict['kind_id'] = 0
                warning_dict['level_id'] = 0