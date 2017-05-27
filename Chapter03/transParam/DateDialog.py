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
	def __init__(self, parent = None):
		super(DateDialog, self).__init__(parent)

		layout = QVBoxLayout(self)

		# nice widget for editing the date
		self.datetime = QDateTimeEdit(self)
		self.datetime.setCalendarPopup(True)
		self.datetime.setDateTime(QDateTime.currentDateTime())
		layout.addWidget(self.datetime)

		# OK and Cancel buttons
		buttons = QDialogButtonBox(
		QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
		Qt.Horizontal, self)
		buttons.accepted.connect(self.accept)
		buttons.rejected.connect(self.reject)
		layout.addWidget(buttons)

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
