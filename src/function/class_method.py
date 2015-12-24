# -*- coding:utf-8 -*-


def create(class_name, file_name='module'):
    m_path = "src." + file_name + "." + class_name + '_' + file_name
    # !!! 根据官方文档 __import__ 函数的第四个参数必须不为空，才能 导入一串import src.xx.xx 否则只导入最上级src
    m = __import__(m_path, {}, {}, ['not None'])
    return getattr(m,  class_name.capitalize() + file_name.capitalize())()