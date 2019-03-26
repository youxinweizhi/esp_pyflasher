
import sys
import os
# os.system('esptool.exe --chip esp32 --port com5 erase_flash')
# os.system('esptool.exe --chip esp32 --port com5 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.binesp32-20190125-v1.10.bin')
# res=os.system("esptool.exe erase_flash")
# os.system('esptool.exe --port com5 --baud 115200 write_flash --flash_size=detect 0 esp8266-20180126-v1.9.3-240-ga275cb0f.bin')
# print(res)
import serial
import serial.tools.list_ports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QToolTip,QMessageBox
from mainWindow import Ui_Form
from PyQt5.QtCore import Qt

#导入图标和字体库
from PyQt5.QtGui import QIcon,QFont
class MyWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)
        #增加图标
        self.setWindowIcon(QIcon('icon.ico'))
        self.Base_PAth=os.getcwd()
        self.get_com()
        self.get_bin()

    def get_com(self):
        port_list = list(serial.tools.list_ports.comports())
        for x in port_list:
            self.comboBox.addItem(list(x)[0])
    def get_bin(self):
        for root,dirs,files in os.walk(os.getcwd()):
            for file in files:
              if os.path.splitext(file)[1] == '.bin':
                self.comboBox_2.addItem(file)
    def test(self):
        self.statusBar().showMessage('开始刷新固件.....')
        com=self.comboBox.currentText()
        firmware=self.comboBox_2.currentText()
        print(com,firmware)
        res=os.system("esptool.exe --port %s --baud 115200 write_flash --flash_size=detect 0 %s " %(com,firmware))
        if res ==0:
            self.statusBar().showMessage('固件刷新成功')
        else:
            self.statusBar().showMessage('固件刷新失败')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
