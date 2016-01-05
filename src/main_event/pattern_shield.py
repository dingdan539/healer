# -*- coding:utf-8 -*-
from interface import *
from pattern_father import *
from ..function.class_method import create


class ShieldAll(Father, InterfaceShield):
    """
        this class must behind the pattern_separate
    """

    def shield(self, warning_dict):
        desc = warning_dict['description']
        clock = warning_dict['clock']
        ip = warning_dict['ip']
        pool_id = warning_dict['pool_id']
        source_id = warning_dict['source_id']

        sql = "select * from shield where %s between start_time and end_time" % (clock, )

        data = self.f_ie_db.execute(sql)

        if data:
            for item in data:
                judge_list = []

                if item['pool_id'] != 0:
                    if item['pool_id'] == pool_id:
                        judge_list.append(False)
                    else:
                        judge_list.append(True)

                if item['ip'] != '':
                    if item['ip'] == ip:
                        judge_list.append(False)
                    else:
                        judge_list.append(True)

                if item['source_id'] != 0:
                    if item['source_id'] == source_id:
                        judge_list.append(False)
                    else:
                        judge_list.append(True)

                if item['key'] != '':
                    if item['key'] in desc:
                        judge_list.append(False)
                    else:
                        judge_list.append(True)

                count = len(judge_list)
                false_count = 0
                for i in judge_list:
                    if not i:
                        false_count += 1
                if (false_count == count) and (false_count != 0):
                    return False
        return True