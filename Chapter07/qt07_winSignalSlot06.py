# -*- coding: utf-8 -*-
"""
    【简介】
    信号槽连接滑块LCD示例


"""

import sys
from PyQt5.QtWidgets import QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication
from PyQt5.QtCore import Qt

class WinForm(QWidget):
    def __init__(self):
        super().__init__()   
        self.initUI()

    def initUI(self):
        #1 先创建滑块和 LCD 部件
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        #2 通过QVboxLayout来设置布局
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)

        self.setLayout(vBox)
        #3 valueChanged()是Qslider的一个信号函数，只要slider的值发生改变，它就会发射一个信号，然后通过connect连接信号的接收部件，也就是lcd。
        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,350,150)
        self.setWindowTitle("信号与槽：连接滑块LCD")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()                      
    sys.exit(app.exec_())
