# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_genetrate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 401)
        self.code_show_textedit = QtWidgets.QTextEdit(Dialog)
        self.code_show_textedit.setGeometry(QtCore.QRect(10, 40, 301, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.code_show_textedit.setFont(font)
        self.code_show_textedit.setObjectName("code_show_textedit")
        self.code_generate_btn = QtWidgets.QPushButton(Dialog)
        self.code_generate_btn.setGeometry(QtCore.QRect(331, 85, 75, 51))
        self.code_generate_btn.setObjectName("code_generate_btn")
        self.code_save_btn = QtWidgets.QPushButton(Dialog)
        self.code_save_btn.setGeometry(QtCore.QRect(331, 234, 75, 51))
        self.code_save_btn.setObjectName("code_save_btn")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 267, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.code_length = QtWidgets.QLineEdit(self.layoutWidget)
        self.code_length.setObjectName("code_length")
        self.horizontalLayout.addWidget(self.code_length)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.code_number = QtWidgets.QLineEdit(self.layoutWidget)
        self.code_number.setObjectName("code_number")
        self.horizontalLayout.addWidget(self.code_number)

        self.retranslateUi(Dialog)
        self.code_generate_btn.clicked.connect(Dialog.code_generate)
        self.code_save_btn.clicked.connect(Dialog.code_save)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "激活码生成器"))
        self.code_generate_btn.setText(_translate("Dialog", "生成激活码"))
        self.code_save_btn.setText(_translate("Dialog", "导出激活码"))
        self.label.setText(_translate("Dialog", "激活码长度"))
        self.code_length.setText(_translate("Dialog", "20"))
        self.label_2.setText(_translate("Dialog", "激活码数量"))
        self.code_number.setText(_translate("Dialog", "10"))

