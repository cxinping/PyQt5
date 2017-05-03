# -*- coding: utf-8 -*-

"""
    【简介】
    部件中的信号槽传递额外参数示例


"""

from PyQt5.QtCore import *  
from PyQt5.QtGui import *  
from PyQt5.QtWidgets import *
import sys 
from functools import partial

class WinForm(QMainWindow):  
	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)  
		button1 = QPushButton('Button 1')  
		button2 = QPushButton('Button 2')  
        
		button1.clicked.connect(lambda: self.onButtonClick(1)) 
		
		button2.clicked.connect(partial(self.onButtonClick, 2))   

		layout = QHBoxLayout()  
		layout.addWidget(button1)  
		layout.addWidget(button2)  
  
		main_frame = QWidget()  
		main_frame.setLayout(layout)       
		self.setCentralWidget(main_frame)  
  
	def onButtonClick(self, n):  
		print('Button {0} 被按下了'.format(n))  
		QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))
             
  
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
