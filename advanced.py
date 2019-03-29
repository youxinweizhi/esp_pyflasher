#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import sys, os, traceback
import esp_config
import threading
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
        res=esp_config.flash(port)
        if res:
            return "固件刷新成功"
        return "固件刷新失败"
    except Exception as e:
        print(traceback.format_exc())
        return "固件刷新失败"

def run(fun1):
    t = threading.Thread(target=fun1)
    t.start()
    return "请等待..."