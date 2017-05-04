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
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)

        self.setLayout(vBox)
        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,350,150)
        self.setWindowTitle("信号槽连接滑块LCD")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
            
    sys.exit(app.exec_())
