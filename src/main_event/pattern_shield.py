# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *


class ShieldIp(Father, InterfaceShield):
    def shield(self, warning_dict):

        return True


class ShieldTime(Father, InterfaceShield):
    def shield(self, warning_dict):

        return False