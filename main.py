#!/usr/bin/env python
# coding: utf-8
'''
@File   :AutoErase.py
@Author :youxinweizhi
@Date   :2019/3/28
@Github :https://github.com/youxinweizhi
'''
import control
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from mainWindow import Ui_Form
from PyQt5.QtGui import QIcon
import threading
mutex = threading.Lock()

class MyWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.main)
        self.checkBox_3.stateChanged.connect(self.disable_op)
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.setWindowIcon(QIcon('./image/icon.ico'))
        self.statusBar().showMessage("https://github.com/youxinweizhi/esp_pyflasher")
        self.get_com()
        self.get_bin()
        self.get_borad()
        self.get_config()

    def get_config(self):
        import config
        config = config.get_confg_dict()

        if 'erase' in config:
            self.checkBox.setCheckState(config['erase'] == 'True')

        if 'advanced' in config:
            self.checkBox_3.setCheckState(config['advanced'] == 'True')

        if 'auto' in config and config['auto'] == 'True':
            self.main()

    def disable_op(self):
        if self.checkBox_3.isChecked():
            self.comboBox_2.setDisabled(True)
            self.comboBox_3.setDisabled(True)
            self.checkBox.setDisabled(True)
        else:
            self.comboBox_2.setDisabled(False)
            self.comboBox_3.setDisabled(False)
            self.checkBox.setDisabled(False)

    def get_com(self):
        self.comboBox.addItems(control.list_serial())

    def check_com(self):
        result = len(self.com) > 1  # and open(com) test
        if result is False:
            self.statusBar().showMessage('The selected serial port is not available')
        return result

    def get_bin(self):
        self.comboBox_2.addItems(control.list_bin())

    def get_borad(self):
        self.comboBox_3.addItems(control.list_board())

    def erase(self):
        self.statusBar().showMessage('Start to erase firmware...')
        self.statusBar().showMessage(control.flash_erase(self.com))
        self.flash()
        self.pushButton.setDisabled(False)

    def flash(self):
        self.statusBar().showMessage('Start to flash firmware...')
        self.statusBar().showMessage(control.flash_bin(self.board, self.com, self.firmware))
        self.pushButton.setDisabled(False)

    def flash_adv(self):
        self.statusBar().showMessage('Start to advanced flash...')
        import advanced
        self.statusBar().showMessage(advanced.flash_bin(self.com))
        self.pushButton.setDisabled(False)

    def main(self):
        self.com = self.comboBox.currentText().split(" - ", 1)[0]
        if self.check_com():
            self.firmware = self.comboBox_2.currentText()
            self.board = self.comboBox_3.currentText()
            print(self.com,self.firmware,self.board)
            self.pushButton.setDisabled(True)
            with mutex:
                task = self.flash_adv if self.checkBox_3.isChecked() else self.erase if self.checkBox.isChecked() else self.flash
                threading.Thread(target=task).start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
