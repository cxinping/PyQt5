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
		dateVal = self.dateEdit.dateTime()
		time = self.timeEdit.time()		
		print('dateVal=%s' % dateVal )   
		print('\n#2 选择时间'  )           
		print('hour=%d' % time.hour() )           
		print('minute=%d' % time.minute() )  
		print('second=%d' % time.hour() )  
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = CalendarExample()
	demo.show()
	sys.exit(app.exec_())
