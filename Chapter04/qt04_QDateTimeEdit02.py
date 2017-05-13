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
		self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
		self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        # 设置最小日期
		self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365)) 
        # 设置最大日期
		self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365)) 
		self.dateEdit.setCalendarPopup( True)

		self.dateEdit.dateChanged.connect(self.onDateChanged) 
		self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged) 
		self.dateEdit.timeChanged.connect(self.onTimeChanged) 
		
		self.btn = QPushButton('获得日期和时间')  
		self.btn.clicked.connect(self.onButtonClick) 
        
		vlayout.addWidget( self.dateEdit )
		vlayout.addWidget( self.btn )
		self.setLayout(vlayout)   

	# 日期发生改变时执行		
	def onDateChanged(self , date):
		print(date)
	
	# 无论日期还是时间发生改变，都会执行
	def onDateTimeChanged(self , dateTime ):
		print(dateTime)
			
	# 时间发生改变时执行
	def onTimeChanged(self , time):
		print(time)			
	
	def onButtonClick(self ):      
		dateTime  = self.dateEdit.dateTime()
		# 最大日期
		maxDate = self.dateEdit.maximumDate() 
		# 最大日期时间
		maxDateTime = self.dateEdit.maximumDateTime() 
		# 最大时间
		maxTime = self.dateEdit.maximumTime() 
		# 最小日期
		minDate = self.dateEdit.minimumDate() 
		# 最小日期时间
		minDateTime = self.dateEdit.minimumDateTime() 
		# 最小时间	
		minTime = self.dateEdit.minimumTime() 
		 
		print('\n选择日期时间'  )  	
		print('dateTime=%s' % str(dateTime) ) 
		print('maxDate=%s' % str(maxDate) ) 
		print('maxDateTime=%s' % str(maxDateTime) ) 
		print('maxTime=%s' % str(maxTime) ) 
		print('minDate=%s' % str(minDate) ) 
		print('minDateTime=%s' % str(minDateTime) ) 
		print('minTime=%s' % str(minTime) ) 
		              
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = DateTimeEditDemo()
	demo.show()
	sys.exit(app.exec_())
