# -*- coding:utf-8 -*-

import sys
from config import *


def main_load():
    from src.common.db.op import *

if __name__ == "__main__":

    config = load_config_auto()

    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sys.path.append(ROOT_PATH)
    main_load()
