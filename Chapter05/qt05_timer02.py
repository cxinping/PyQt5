# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中关闭应用例子
 
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
if __name__ == '__main__':
	app = QApplication(sys.argv)
	label = QLabel("<font color=red size=128><b>Hello PyQT，窗口会在10秒后消失！</b></font>")
	label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
	label.show()

    # 设置10s后自动退出
	QTimer.singleShot(10000, app.quit) 
	sys.exit(app.exec_())
