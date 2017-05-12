# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QDateEdit, QTimeEdit 例子
   
  
'''

import sys
#from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,  QTime 

class CalendarExample( QWidget):
	def __init__(self):
		super(CalendarExample, self).__init__()
		self.initUI()
		
	def initUI(self): 
		self.setWindowTitle('QDateEdit,QTimeEdit例子')
		self.resize(300, 90)   

		vlayout = QVBoxLayout()
		self.dateEdit = QDateEdit(QDate.currentDate(), self)
        # 设置最小日期
		self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365)) 
        # 设置最大日期
		self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365)) 
		self.dateEdit.setCalendarPopup( True)
		
		self.timeEdit = QTimeEdit(QTime.currentTime(), self)
		self.timeEdit.setDisplayFormat("HH:mm:ss")
		self.btn = QPushButton('获得日期和时间')  
		self.btn.clicked.connect(self.onButtonClick) 
        
		vlayout.addWidget( self.dateEdit )
		vlayout.addWidget( self.timeEdit )
		vlayout.addWidget( self.btn )
		self.setLayout(vlayout)   
		
	def onButtonClick(self ):      
		dateTime  = self.dateEdit.dateTime()
		#最大日期
		maxDate = self.dateEdit.maximumDate() 
		#最大日期时间
		maxDateTime = self.dateEdit.maximumDateTime() 
		#最大时间
		maxTime = self.dateEdit.maximumTime() 
		#最小日期
		minDate = self.dateEdit.minimumDate() 
		#最小日期时间
		minDateTime = self.dateEdit.minimumDateTime() 
		#最小时间	
		minTime = self.dateEdit.minimumTime() 
		
		time = self.timeEdit.time()	
		print('\n#1 选择日期'  )  	
		print('dateTime=%s' % str(dateTime) ) 
		print('maxDate=%s' % str(maxDate) ) 
		print('maxDateTime=%s' % str(maxDateTime) ) 
		print('maxTime=%s' % str(maxTime) ) 
		print('minDate=%s' % str(minDate) ) 
		print('minDateTime=%s' % str(minDateTime) ) 
		print('minTime=%s' % str(minTime) ) 
		
		print('\n#2 选择时间'  )           
		print('hour=%d' % time.hour() )           
		print('minute=%d' % time.minute() )  
		print('second=%d' % time.hour() )  
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = CalendarExample()
	demo.show()
	sys.exit(app.exec_())
