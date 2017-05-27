# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog 
from MainForm import Ui_MainWindow  
from ChildrenForm import Ui_ChildrenForm  

class MainForm( QMainWindow , Ui_MainWindow):  
	def __init__(self):  
		super(MainForm,self).__init__()  
		self.setupUi(self)  
		
		# self.child = children()生成子窗口实例self.child  
		self.child = ChildrenForm()                          
		# 菜单的点击事件是triggered      
		self.closeMainWinAction.triggered.connect(self.close)  
		# 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中 
		self.addSubWinAction.triggered.connect(self.childShow)    

	def childShow(self): 
		# 添加子窗口
		self.MaingridLayout.addWidget(self.child)            
		self.child.show()  

	def openMsg(self):  
		file,ok= QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)") 
		# 在状态栏显示文件地址  		
		self.statusbar.showMessage(file)                   
  
class ChildrenForm( QWidget, Ui_ChildrenForm):  
	def __init__(self):  
		super(ChildrenForm,self).__init__()  
		self.setupUi(self)  
  
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec_()) 
