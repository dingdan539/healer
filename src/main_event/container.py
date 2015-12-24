# -*- coding:utf-8 -*-


class Container(object):
    __shield_list = []
    __separate_list = []

    def set_shield(self, shield_cls):
        self.__shield_list.append(shield_cls)

    def set_separate(self, separate_cls):
        self.__separate_list.append(separate_cls)

    def shield_perform(self, warning_dict):
        for c in self.__shield_list:
            if not c.shield(warning_dict):
                return False
        return True

    def separate_perform(self, warning_dict):
        for c in self.__separate_list:
            warning_dict = c.separate(warning_dict)
        return warning_dict


