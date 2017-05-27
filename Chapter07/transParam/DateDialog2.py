# -*- coding: utf-8 -*-

'''
    【简介】
 
    对话框关闭时返回值给主窗口 例子
  
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
	Signal_OneParameter = pyqtSignal(str)
	 
	def __init__(self, parent = None):
		super(DateDialog, self).__init__(parent)
		self.setWindowTitle('对话框关闭时返回值给主窗口例子') 	
		
		# 在布局中添加部件
		layout = QVBoxLayout(self)
		self.datetime = QDateTimeEdit(self)
		self.datetime.setCalendarPopup(True)
		self.datetime.setDateTime(QDateTime.currentDateTime())
		self.lineedit = QLineEdit(self)
		self.btn = QPushButton('发射信号')
		layout.addWidget(self.lineedit)
		layout.addWidget(self.datetime)
		layout.addWidget(self.btn)

		# 使用两个button(ok和cancel)分别连接accept()和reject()槽函数
		buttons = QDialogButtonBox(
			QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
			Qt.Horizontal, self)
		buttons.accepted.connect(self.accept)
		buttons.rejected.connect(self.reject)
		layout.addWidget(buttons)

		self.datetime.dateTimeChanged.connect( self.showDate )
		self.btn.clicked.connect( self.handleTimeFun )
				
	@pyqtSlot()
	def handleTimeFun(self):
		self.Signal_OneParameter.emit((self.datetime.dateTime()).toString())
		self.lineedit.setText(str((self.datetime.dateTime()).toString()))
    
	@pyqtSlot(QDateTime)	
	def showDate(self,datetime):
		self.lineedit.setText(datetime.toString())
		self.update()
		    
	# 从对话框中获取当前日期和时间
	def dateTime(self):
		return self.datetime.dateTime()
		
    # 静态方法创建对话框并返回 (date, time, accepted)
	@staticmethod
	def getDateTime(parent = None):
		dialog = DateDialog(parent)
		result = dialog.exec_()
		date = dialog.dateTime()
		return (date.date(), date.time(), result == QDialog.Accepted)
		
		
		
		
		
		
		
