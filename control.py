# coding:utf-8
import os
import serial.tools.list_ports
import threading

def list_serial():
    port_list = list(serial.tools.list_ports.comports())
    return [str(x[0]) for x in port_list]

def list_bin():
    result = []
    for root, dirs, files in os.walk(os.getcwd()):
        result += [file for file in files if os.path.splitext(file)[1] == '.bin']
    # print(result)
    return result

def flash_erase(com):
    res=os.system("esptool.exe --port %s erase_flash" %com)
    if res ==0:
        status='Flash已经清空'
    else:
        status='Flash清空失败'
    return status

def flash_bin(st,com,firmware):
    if st:
        res=os.system("esptool.exe --port %s --baud 115200 write_flash --flash_size=detect 0 %s " %(com,firmware))
    else:
        res=os.system("esptool.exe --chip esp32 --port %s --baud 115200 write_flash -z 0x1000  %s " %(com,firmware))
    if res ==0:
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



# def flash_bin(serialName):
#     import config
#     os.system(config.esptool_cmd)
#     pass
#
# try:
#     print("Looking for upload port...")
#     plist = list(serial.tools.list_ports.comports())
#
#     serialName = ''
#
#     if len(plist) <= 0:
#         print("Serial Not Found!")
#     else:
#         plist_0 = list(plist[len(plist) - 1])
#         serialName = plist_0[0]
#         print("Auto-detected:" + serialName)
#
#     FLASH_MODE = "dio"
#     FLASH_FREQ = "40m"
#
#     FLASH_START = "0x1000"
#
#     from esptool import main
#
#     import sys
#
#     bak = sys.argv
#
#     sys.argv = [
#             'AutoFlash.py', '--chip', 'esp32',
#             '--port', serialName,
#             '--baud', '460800', # 921600
#             'write_flash', '-z',
#             '--flash_mode', FLASH_MODE,
#             '--flash_size', '4MB',
#             '--flash_freq', FLASH_FREQ,
#             FLASH_START, 'firmware.bin'
#     ]
#
#     try:
#             pos = bak.index('--port')
#             if pos is not False:
#                     sys.argv[4] = bak[pos + 1]
#     except ValueError:
#             pass
#
#     try:
#             pos = bak.index('--baud')
#             if pos is not False:
#                     sys.argv[6] = bak[pos + 1]
#     except ValueError:
#             pass
#
#     # print(sys.argv)
#
#     main()
# except Exception as e:
#     print(e)
