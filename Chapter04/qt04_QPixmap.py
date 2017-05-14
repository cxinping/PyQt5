# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QPixmap 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = QWidget()
	lab1 = QLabel()
	lab1.setPixmap(QPixmap("./images/python.jpg"))
	vbox=QVBoxLayout()
	vbox.addWidget(lab1)
	win.setLayout(vbox)
	win.setWindowTitle("QPixmap 例子")
	win.show()
	sys.exit(app.exec_())
