# -*- coding:utf-8 -*-
"""
    description:
        目前没有实现交换机和路由器，以后需要再改进
"""
qmaps = {
    'zabbix_event_queue': {
        'prefix': 'REDIS_',
        'exchange': '',  # 定义交换机
        'route': ''      # 定义路由关键字
    },
    'zabbix_stability_queue': {
        'prefix': 'REDIS_',
        'exchange': '',  # 定义交换机
        'route': ''      # 定义路由关键字
    }
}