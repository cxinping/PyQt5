# -*- coding: utf-8 -*-

"""
    【简介】
    部件中的信号槽通信示例


"""

from PyQt5.QtCore import *  
from PyQt5.QtGui import *  
from PyQt5.QtWidgets import *
import sys 
      
class MyForm(QMainWindow):  
	def __init__(self, parent=None):  
		super(MyForm, self).__init__(parent)  
		button1 = QPushButton('Button 1')  
		button2 = QPushButton('Button 1')  
		button1.clicked.connect(lambda: self.on_button(1))  
		button2.clicked.connect(lambda: self.on_button(2))  
  
		layout = QHBoxLayout()  
		layout.addWidget(button1)  
		layout.addWidget(button2)  
  
		main_frame = QWidget()  
		main_frame.setLayout(layout)  
  
		self.setCentralWidget(main_frame)  
  
	def on_button(self, n):  
		print('Button {0} clicked'.format(n))  
  
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = MyForm()  
	form.show()  
	app.exec_()  
