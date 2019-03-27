# -*- coding: utf-8 -*-
#by:youxinweizhi
#QQ:416895063
import control
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
        self.comboBox.addItems(control.list_serial())
    def get_bin(self):
        self.comboBox_2.addItems(control.list_bin())

    def erase_flash(self):
        # self.statusBar().showMessage('清空flash.....')
        self.statusBar().showMessage(control.flash_erase(self.com))
        self.flasher()
    def flasher(self):
        self.statusBar().showMessage('开始刷新固件')
        self.statusBar().showMessage(control.flash_bin(self.checkBox_2.isChecked(),self.com,self.firmware))

    def main(self):
        self.com=self.comboBox.currentText()
        self.firmware=self.comboBox_2.currentText()
        # if self.checkBox.isChecked():
        #     self.statusBar().showMessage('清空flash.....')
        #     t1=threading.Thread(target=self.erase_flash)
        #     t1.start()
        # else:
        #     # self.status='开始刷新固件.....'
        #     self.statusBar().showMessage(self.status)
        #     t=threading.Thread(target=self.flasher)
        #     t.start()

        self.statusBar().showMessage(control.run(self.checkBox.isChecked(),self.erase_flash,self.flasher))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
