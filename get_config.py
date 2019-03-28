#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import sys, os, traceback
import esptool

# print(sys.path) # 查找依赖的目录
cwd = os.getcwd()
# print(cwd, os.listdir()) # 定位到打开目录 而不是解压后的临时目录
sys.path.append(os.getcwd())

try:
    exec("import esp_config")
except Exception as e:
    print(traceback.format_exc())

def flash_bin(port):
    try:
        esp_config.flash(port)
    except Exception as e:
        return traceback.format_exc()

if __name__ == '__main__':
    print(flash_bin('com3'))
    import esp_config
    esp_config.flash('com3')
