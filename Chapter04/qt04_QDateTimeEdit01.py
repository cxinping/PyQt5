# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 DateTimeEdit 例子
   
  
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,   QDateTime , QTime 

class DateTimeEditDemo(QWidget):
	def __init__(self):
		super(DateTimeEditDemo, self).__init__()
		self.initUI()
		
	def initUI(self): 
		self.setWindowTitle('QDateTimeEdit例子')
		self.resize(300, 90)   

		vlayout = QVBoxLayout()
		dateTimeEdit = QDateTimeEdit(self)
		dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
		dateEdit = QDateTimeEdit(QDate.currentDate(), self)
		timeEdit = QDateTimeEdit(QTime.currentTime(), self)

		# 设置日期时间格式
		dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
		dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
		dateEdit.setDisplayFormat("yyyy.MM.dd")
		timeEdit.setDisplayFormat("HH:mm:ss")
                
		vlayout.addWidget( dateTimeEdit )
		vlayout.addWidget( dateTimeEdit2)
		vlayout.addWidget( dateEdit )
		vlayout.addWidget( timeEdit )		
		self.setLayout(vlayout)   
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DateTimeEditDemo()
	demo.show()
	sys.exit(app.exec_())
