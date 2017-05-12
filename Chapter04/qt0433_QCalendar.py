# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QCalendarWidget 例子
   
  
'''

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CalendarExample( QWidget):
	def __init__(self):
		super(CalendarExample, self).__init__()
		self.initUI()
		
	def initUI(self): 
		cal =  QCalendarWidget(self)
		cal.setGridVisible(True)
		cal.move(20, 20)
		cal.clicked[QtCore.QDate].connect(self.showDate)
		self.lbl =  QLabel(self)
		date = cal.selectedDate()
		self.lbl.setText(date.toString("yyyy-MM-dd dddd"))
		self.lbl.move(20, 300)
		self.setGeometry(100,100,400,400)
		self.setWindowTitle('Calendar 例子')
		
	def showDate(self, date): 
		self.lbl.setText(date.toString("yyyy-MM-dd dddd") )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = CalendarExample()
	demo.show()
	sys.exit(app.exec_())
