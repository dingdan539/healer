# -*- coding:utf-8 -*-
import os
import platform


def load_config_auto():
    system_name = platform.system()
    if system_name == "Windows":
        return load_config("devel")
    elif system_name == "Linux":
        return load_config("deploy")


def load_config(mode):
    """加载配置项"""
    try:
        if mode == "devel":
            from .devel import DevelConfig
            return DevelConfig

        elif mode == "deploy":
            from .deploy import DeployConfig
            return DeployConfig

        else:
            from .default import Config

    except Exception as e:
        print e
