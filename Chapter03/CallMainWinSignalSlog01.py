# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from MainWinSignalSlog01 import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
	def __init__(self, parent=None):    
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		# 槽函数不用加括号
		self.closeWinBtn.clicked.connect(self.printInfo)   
	
	# 定义槽
	def printInfo(self):                               
		print("hello PyQt !!! ")
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	myWin = MyMainWindow()  
	myWin.show()  
	sys.exit(app.exec_())  
