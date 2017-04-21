# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon 

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.setWindowTitle("界面背景图片设置") 
		self.resize(350,  250)  
		self.setObjectName("MainWindow")
		self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")
       
if __name__ == "__main__": 
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())
