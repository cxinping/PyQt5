# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中QTimer例子
 
  
'''

from PyQt5.QtWidgets import QWidget,  QPushButton ,  QApplication ,QListWidget,  QGridLayout , QLabel
from PyQt5.QtCore import QTimer
import sys 
import time

class WinForm(QWidget):  
	
	def __init__(self,parent=None): 
		super(WinForm,self).__init__(parent) 
		self.listFile= QListWidget() 
		self.label = QLabel('显示当前时间')
		self.startBtn = QPushButton('开始') 
		self.endBtn = QPushButton('结束') 
		layout = QGridLayout(self) 
		
		#self.timer = QTimer(self) #初始化一个定时器
		#self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
		#self.timer.start(2000) #设置计时间隔并启动

		layout.addWidget(self.label,0,0,1,2) 

		layout.addWidget(self.startBtn,1,0) 
		layout.addWidget(self.endBtn,1,1) 		
		
		self.startBtn.clicked.connect( self.startTimer) 
		self.endBtn.clicked.connect( self.endTimer) 
				
		self.setLayout(layout)   
		
	def slotAdd(self): 
		for n in range(10): 
			str_n='File index {0}'.format(n) 
			self.listFile.addItem(str_n) 
			QApplication.processEvents() 
			time.sleep(1) 

	def startTimer(self): 
		print('--- startTimer ')

	def endTimer(self): 
		print('--- endTimer ')
	
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
