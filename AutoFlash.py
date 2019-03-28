# coding:utf-8

def run(com,esp_type,firmware):
    FLASH_START = "0x1000"
    FLASH_MODE = "dio"
    FLASH_FREQ = "40m"
    from esptool import main
    import sys
    if esp_type=="esp8266":
        sys.argv = [
                'AutoFlash.py',
                '--port', com,
                '--baud', '460800',
                'write_flash',"--flash_size=detect", '0',
                'esp8266-20180126-v1.9.3-240-ga275cb0f.bin'
        ]
    else:
        sys.argv = [
                'AutoFlash.py', '--chip', 'esp32',
                '--port', com,
                '--baud', '460800',
                'write_flash', '-z',
                '--flash_mode', FLASH_MODE,
                '--flash_size', '4MB',
                '--flash_freq', FLASH_FREQ,
                FLASH_START, firmware
        ]
    try:
        main()
        return True
    except:
        return False
