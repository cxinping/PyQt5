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
	l1=QLabel()
	l1.setPixmap(QPixmap("./images/python.jpg"))
	vbox=QVBoxLayout()
	vbox.addWidget(l1)
	win.setLayout(vbox)
	win.setWindowTitle("QPixmap Demo")
	win.show()
	sys.exit(app.exec_())