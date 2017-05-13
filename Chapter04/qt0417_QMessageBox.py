# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QMessage 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWindow( QWidget):  
	def __init__(self):  
		super(MyWindow,self).__init__()  
		self.myButton = QPushButton(self)  
		self.myButton.setObjectName("myButton")  
		self.myButton.setText("Test")  
		self.myButton.clicked.connect(self.msg)  

	def msg(self):  
		  #使用infomation信息框  
		reply = QMessageBox.information(self, "标题", "消息", QMessageBox.Yes | QMessageBox.No)  
		print( reply )
		
if __name__ == '__main__':
	app= QApplication(sys.argv)    
	myshow=MyWindow()  
	myshow.show() 
	sys.exit(app.exec_())
