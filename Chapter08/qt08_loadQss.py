# -*- coding: utf-8 -*-
"""
    【简介】
	 加载QSS文件
     
"""
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
		vbox = QVBoxLayout()
		vbox.addWidget( btn1 )
      
		self.setLayout(vbox) 
       
if __name__ == "__main__": 
	app = QApplication(sys.argv)
	win = MainWindow()
    
	styleFile = './style.qss'
	qssStyle = CommonHelper.readQss( styleFile )	
	win.setStyleSheet( qssStyle ) 
	win.show()     
	sys.exit(app.exec_())
