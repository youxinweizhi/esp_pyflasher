#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''

import os
import serial.tools.list_ports
import AutoErase
import AutoFlash

def list_serial():
    port_list = list(serial.tools.list_ports.comports())
    return [str(x) for x in port_list]

def list_board():
    borad_list = ['esp32', 'esp8266']
    return [str(x) for x in borad_list]


def list_bin():
    result = []
    for root, dirs, files in os.walk(os.getcwd()):
        result += [file for file in files if os.path.splitext(file)[1] == '.bin']
    # print(result)
    return result

def flash_erase(com):
    print(com)
    res = AutoErase.run(com)
    return 'Erase success.' if res is None else res

def flash_bin(board, com, firmware):
    print(board, com, firmware)
    res = AutoFlash.run(com, esp_type=board, firmware=firmware)
    return 'Burn success.' if res is None else res

if __name__ == '__main__':
    flash_erase("COM3")
    flash_bin("esp32", "COM3", "firmware.bin")
