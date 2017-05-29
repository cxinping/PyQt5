# -*- coding: utf-8 -*-

import sys  
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget 
  
class WinForm( QWidget):  
	def __init__(self,  parent = None):  
		super(WinForm,self).__init__(parent)    
		self.setGeometry(300,  300,  350,  350)  
		self.setWindowTitle('点击按钮关闭窗口')  
		quit = QPushButton('Close',  self)  
		quit.setGeometry(10,  10,  60,  35)  
		quit.setStyleSheet("background-color: red")           
		quit.clicked.connect(self.close)  
          
if __name__ == "__main__":  
	app = QApplication(sys.argv)   
	win = WinForm()        
	win.show()  
	sys.exit(app.exec_())  
