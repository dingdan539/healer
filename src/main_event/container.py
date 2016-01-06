# -*- coding:utf-8 -*-


class Container(object):
    __shield_list = []  # 顺序遍历
    __separate_list = []  # 顺序遍历
    __output_list = []  # 顺序遍历
    __process_list = []  # 非并发，顺序遍历, 多择其一

    def set_shield(self, shield_cls):
        self.__shield_list.append(shield_cls)

    def set_separate(self, separate_cls):
        self.__separate_list.append(separate_cls)

    def set_output(self, output_cls):
        self.__output_list.append(output_cls)

    def set_process(self, process_cls):
        self.__process_list.append(process_cls)

    def shield_perform(self, warning_dict):
        for c in self.__shield_list:
            if not c.shield(warning_dict):
                return False
        return True

    def separate_perform(self, warning_dict):
        for c in self.__separate_list:
            c.separate(warning_dict)
        return warning_dict

    def output_perform(self, warning_dict):
        for c in self.__output_list:
            c.output(warning_dict)

    def process_perform(self, warning_dict):
        for c in self.__process_list:
            res = c.process(warning_dict)
            if res:
                break