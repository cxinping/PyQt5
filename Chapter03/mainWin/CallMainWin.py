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
		# 菜单的点击事件，当点击关闭菜单时连接槽函数 close()     
		self.fileCloseAction.triggered.connect(self.close)  
		# 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()     
		self.fileOpenAction.triggered.connect(self.openMsg)    

	def openMsg(self):  
		file,ok= QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)") 
		# 在状态栏显示文件地址  		
		self.statusbar.showMessage(file)                   
    
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainForm()  
	win.show()  
	sys.exit(app.exec_()) 
