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
		self.resize(400, 90)
		self.setWindowTitle('对话框关闭时返回值给主窗口例子') 		

		self.open_btn = QPushButton('弹出对话框')
		self.lineEdit1 = QLineEdit(self)
		self.lineEdit2 = QLineEdit(self )
		self.open_btn.clicked.connect( self.openDialog)

		self.lineEdit1.setText('接收时间') 		
		self.lineEdit2.setText('接收时间') 	
		
		grid = QGridLayout()
		grid.addWidget(self.lineEdit1)
		grid.addWidget(self.lineEdit2)
		
		grid.addWidget(self.open_btn)
		self.setLayout(grid)

	def openDialog(self):
		dialog = DateDialog(self)			
		dialog.datetime.dateTimeChanged.connect( self.getDate  )
		dialog.Signal_OneParameter.connect(self.getStrDate)		
		dialog.show()

	@pyqtSlot(str)
	def getStrDate(self,dateStr):
		self.lineEdit1.setText(dateStr)
		
	@pyqtSlot(QDateTime)
	def getDate(self,date):
		print('--- getDate ---')
		self.lineEdit2.setText(date.toString())
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
