# -*- coding: utf-8 -*-

'''
    【简介】
 
    对话框关闭时返回值给主窗口 例子
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
	Signal_OneParameter = pyqtSignal(str)
	 
	def __init__(self, parent = None):
		super(DateDialog, self).__init__(parent)
		self.setWindowTitle('DateDialog') 	
		
		layout = QVBoxLayout(self)

		self.datetime = QDateTimeEdit(self)
		self.datetime.setCalendarPopup(True)
		self.datetime.setDateTime(QDateTime.currentDateTime())
		self.lineedit = QLineEdit(self)
		self.btn = QPushButton('emit signal')
		layout.addWidget(self.lineedit)
		layout.addWidget(self.datetime)
		layout.addWidget(self.btn)

		# OK and Cancel buttons
		buttons = QDialogButtonBox(
			QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
			Qt.Horizontal, self)
		buttons.accepted.connect(self.accept)
		buttons.rejected.connect(self.reject)
		layout.addWidget(buttons)

		self.datetime.dateTimeChanged.connect( self.showDate )
		self.datetime.dateTimeChanged.connect( self.showDate )
		self.btn.clicked.connect( self.myfunc )
		
		buttons.accepted.connect( self.clickOkBtn )
		buttons.rejected.connect( self.clickCancelBtn )		

	def clickOkBtn(self):
		print('--- clickOkBtn ---')
		self.Signal_OneParameter.emit('ok')
		
	def clickCancelBtn(self):
		print('--- clickCancelBtn ---')
		self.Signal_OneParameter.emit('cancel')
		
	@pyqtSlot()
	def myfunc(self):
		self.Signal_OneParameter.emit((self.datetime.dateTime()).toString())
		self.lineedit.setText(str((self.datetime.dateTime()).toString()))
    
	@pyqtSlot(QDateTime)	
	def showDate(self,datetime):
		self.lineedit.setText(datetime.toString())
		self.update()
		    
	# get current date and time from the dialog
	def dateTime(self):
		return self.datetime.dateTime()
		
    # static method to create the dialog and return (date, time, accepted)
	@staticmethod
	def getDateTime(parent = None):
		dialog = DateDialog(parent)
		result = dialog.exec_()
		date = dialog.dateTime()
		return (date.date(), date.time(), result == QDialog.Accepted)
		
		
		
		
		
		
		
