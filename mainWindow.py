# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(334, 125)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 10, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 40, 211, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(250, 60, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 60, 71, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(110, 60, 71, 21))
        self.checkBox_3.setObjectName("checkBox_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " Mpyflasher"))
        self.pushButton.setText(_translate("Form", "Flash"))
        self.label.setText(_translate("Form", "串口："))
        self.label_3.setText(_translate("Form", "固件："))
        self.checkBox.setText(_translate("Form", "eraseflash"))
        self.checkBox_2.setText(_translate("Form", "esp8266"))
        self.checkBox_3.setText(_translate("Form", "Auto"))
