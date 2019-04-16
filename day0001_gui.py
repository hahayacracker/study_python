#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:00
# @Author  : hahaya
# @Site    : 
# @File    : day0001_gui.py
# @Software: PyCharm
# @Note    : day0001的GUI版本,界面使用pyqt实现

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from code_genetrate import Ui_Dialog
import random
str_select = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Win(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def code_generate(self):
        if win.code_length.text()=='' or win.code_number.text()=='':
            QMessageBox.warning(self, "提示","请先填写激活码长度和激活码数量在进行生成", QMessageBox.Ok)
            return
        length = int(win.code_length.text())
        number = int(win.code_number.text())
        self.code_show_textedit.setHtml('')
        for x in range(number):
            code =''
            for y in range(length):
                code += random.choice(str_select)
            print(code)
            self.code_show_textedit.append(code)


    @pyqtSlot()
    def code_save(self):
        codes = self.code_show_textedit.toPlainText()
        if codes =='':
            QMessageBox.warning(self, "提示", "请先生成激活码再进行导出操作", QMessageBox.Ok)
            return
        file_name,_ = QFileDialog.getSaveFileName(self,'保存激活码', 'c:\\',"Text Files(*.txt)")
        print(file_name)
        #一定要注意文件打开的模式 开始用w+模式导出时程序就崩溃
        file = open(file_name,'a+')
        file.writelines(codes)
        file.flush()
        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())
