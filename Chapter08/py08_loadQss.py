# -*- coding: utf-8 -*-
"""
    【简介】
	 加载QSS文件
     
"""
from PyQt5.QtCore import Qt 
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication,  QVBoxLayout , QPushButton
from CommonHelper import CommonHelper

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.resize(477, 258) 
		self.setWindowTitle("加载QSS文件") 
		btn1 = QPushButton( self)  
		btn1.setText('添加')
		btn1.setToolTip('测试提示')
		vbox=QVBoxLayout()
		vbox.addWidget( btn1 )
      
		self.setLayout(vbox) 
       
if __name__ == "__main__": 
	app = QApplication(sys.argv)
	win = MainWindow()
    
	styleFile = './main.qss'
	style = CommonHelper.readQss( styleFile )
	
	win.setStyleSheet( style ) 
	win.setObjectName("MainWindow") 
	win.show()
    
	sys.exit(app.exec_())
