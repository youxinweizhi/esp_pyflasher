#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''

def run(com):

    FLASH_START = "0x1000"
    FLASH_MODE = "dio"
    FLASH_FREQ = "40m"

    import sys
    sys.argv = [
        'AutoFlash.py', '--chip', 'esp32',
        '--port', com,
        '--baud', '460800',
        'write_flash', '-z',
        '--flash_mode', FLASH_MODE,
        '--flash_size', '4MB',
        '--flash_freq', FLASH_FREQ,
        FLASH_START, 'ts'
    ]
    try:
        from esptool import main
        main()
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    run('com3')