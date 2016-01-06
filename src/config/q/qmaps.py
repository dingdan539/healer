# -*- coding:utf-8 -*-
"""
    description:
        目前没有实现交换机和路由器，以后需要再改进
"""
qmaps = {
    """收集存放所有报警信息队列"""
    'zabbix_event_queue': {
        'prefix': 'RMQ_',
        'exchange': '',  # 定义交换机
        'route': ''      # 定义路由关键字
    },
    """稳定性报警专用处理队列"""
    'zabbix_stability_queue': {
        'prefix': 'RMQ_',
        'exchange': '',  # 定义交换机
        'route': ''      # 定义路由关键字
    }
}