#!/usr/bin/env python
# coding: utf-8
'''
@File   :control.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import os
import serial.tools.list_ports
import threading
import AutoErase
import AutoFlash
def list_serial():
    port_list = list(serial.tools.list_ports.comports())
    return [str(x[0]) for x in port_list]

def list_bin():
    result = []
    for root, dirs, files in os.walk(os.getcwd()):
        result += [file for file in files if os.path.splitext(file)[1] == '.bin']
    return result


def flash_erase(com):
    # res=os.system("esptool.exe --port %s erase_flash" %com)
    res=AutoErase.run(com)
    if res:
        status='Flash已经清空'
    else:
        status='Flash清空失败'
    return status

def flash_bin(st,com,firmware):
    if st:
        # res=os.system("esptool.exe --port %s --baud 115200 write_flash --flash_size=detect 0 %s " %(com,firmware))
        res=AutoFlash.run(com,esp_type="esp8266",firmware=firmware)
    else:
        # res=os.system("esptool.exe --chip esp32 --port %s --baud 115200 write_flash -z 0x1000  %s " %(com,firmware))
        res=AutoFlash.run(com,esp_type="esp32",firmware=firmware)
    if res:
        status='固件刷新成功'
    else:
        status='固件刷新失败'
    return status


def run(st,fun1,fun2):
    if st:
        t1=threading.Thread(target=fun1)
        t1.start()
    else:
        t=threading.Thread(target=fun2)
        t.start()
    return "请等待！"