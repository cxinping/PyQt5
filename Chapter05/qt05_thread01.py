# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中 QThread 例子
 
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

global sec
sec=0

def setTime():
	global  sec
	sec+=1
	lcdNumber.display(sec)          #LED显示数字+1

def work():
	timer.start(1000)               #计时器每秒计数
	for i in range(2000000000):
		pass
	
	timer.stop()

if __name__ == "__main__":  	
	app = QApplication(sys.argv) 
	top=QWidget()
	layout=QVBoxLayout(top)             #垂直布局类QVBoxLayout；
	lcdNumber=QLCDNumber()              #加个显示屏
	layout.addWidget(lcdNumber)
	button=QPushButton("测试")
	layout.addWidget(button)

	timer=QTimer()
	timer.timeout.connect(setTime)      #每次计时结束，触发setTime
	button.clicked.connect(work)

	top.show()
	sys.exit(app.exec_())
