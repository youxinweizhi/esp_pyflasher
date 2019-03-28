# coding:utf-8
def run(com):
    from esptool import main
    import sys
    bak = sys.argv
    sys.argv = [
        'AutoFlash.py',
        '--port', com,
        '--baud', '460800',
        'erase_flash'
    ]
    try:
        main()
        return True
    except:
        return False
