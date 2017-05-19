# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中单元格的宽度和高度例子
 
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	label = QLabel("<font color=red size=128><b>Hello PyQT!</b></font>")
	label.show()
	window.resize(500, 500)
	window.move(300, 300)
	window.setWindowTitle('hello PyQt5')
	window.show()

    # 设置10s后自动退出
	QTimer.singleShot(10000, app.quit) 
	sys.exit(app.exec_())
