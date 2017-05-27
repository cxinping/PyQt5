# -*- coding: utf-8 -*-

'''
    【简介】
     对话框关闭时返回值给主窗口例子
    
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog2 import DateDialog

class WinForm(QWidget):  
	
	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)
		self.resize(500, 100)
		self.setWindowTitle('对话框关闭时返回值给主窗口例子') 		

		self.open_btn = QPushButton('OPEN')
		self.le_btn = QLineEdit(self)
		self.le1_btn = QLineEdit(self )
		self.le2_btn = QLineEdit(self )
		self.le3_btn = QLineEdit(self )
		self.open_btn.clicked.connect( self.openDialog)

		self.le_btn.setText('le_btn') 		
		self.le1_btn.setText('le1_btn') 	
		self.le2_btn.setText('le2_btn') 	
		self.le3_btn.setText('le3_btn') 	
		
		grid = QGridLayout()
		grid.addWidget(self.le_btn)
		grid.addWidget(self.le1_btn)
		grid.addWidget(self.le2_btn)
		grid.addWidget(self.le3_btn)
		grid.addWidget(self.open_btn)
		self.setLayout(grid)

	def openDialog(self):
		dialog = DateDialog(self)
		#self.connect(dialog,SIGNAL('sendDate(QDateTime)'),self,SLOT('receiveDate(QDateTime)'))
		#self.connect(dialog,SIGNAL('sendDate(QDateTime)'),self,SLOT('copyDate(QDateTime)'))
		#self.connect(dialog.datetime,SIGNAL('dateTimeChanged(QDateTime)'),self,SLOT('getDate(QDateTime)'))
		#self.connect(dialog,SIGNAL('Signal_OneParameter_Overload(str)'),self,SLOT('getStrDate(str)'))
		
		dialog.datetime.dateTimeChanged.connect( self.getDate  )
		#dialog.Signal_OneParameter.connect(self.getStrDate)
		
		dialog.show()

	@pyqtSlot(str)
	def getStrDate(self,dateStr):
		self.le3_btn.setText(dateStr)
		
	@pyqtSlot(QDateTime)
	def receiveDate(self,date):
		self.le_btn.setText(date.toString())

	@pyqtSlot(QDateTime)
	def getDate(self,date):
		print('--- getDate ---')
		self.le2_btn.setText(date.toString())
		
	@pyqtSlot(QDateTime)
	def copyDate(self,date):
		self.le1_btn.setText(date.toString())
			
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
