# -*- coding: utf-8 -*-
#by:youxinweizhi
#QQ:416895063
import serial
import serial.tools.list_ports
import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_Form
import threading
#导入图标和字体库
from PyQt5.QtGui import QIcon,QFont

class MyWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main)
        self.setWindowIcon(QIcon('icon.ico'))
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
    def erase_flash(self):
        res=os.system("esptool.exe --port %s erase_flash " %(self.com))
        if res ==0:
            self.status='Flash已经清空'
            self.statusBar().showMessage(self.status)
        else:
            self.status='Flash清空失败'
            self.statusBar().showMessage(self.status)
        self.statusBar().showMessage('开始刷新固件')
        self.flasher()
    def flasher(self):
        if self.checkBox.isChecked():
            res=os.system("esptool.exe --port %s --baud 115200 write_flash --flash_size=detect 0 %s " %(self.com,self.firmware))
        else:
            res=os.system("esptool.exe --chip esp32 --port %s --baud 115200 write_flash -z 0x1000  %s " %(self.com,self.firmware))

        if res ==0:
            self.status='固件刷新成功'
            self.statusBar().showMessage(self.status)

        else:
            self.status='固件刷新失败'
            self.statusBar().showMessage(self.status)
    def main(self):
        self.com=self.comboBox.currentText()
        self.firmware=self.comboBox_2.currentText()
        if self.checkBox.isChecked():
            self.status='清空flash.....'
            self.statusBar().showMessage(self.status)
            t1=threading.Thread(target=self.erase_flash)
            t1.start()
        else:
            self.status='开始刷新固件.....'
            self.statusBar().showMessage(self.status)
            t=threading.Thread(target=self.flasher)
            t.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
