# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中QButton例子
    
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)
		layout = QVBoxLayout()

		self.btn1 = QPushButton("Button1")
		self.btn1.setCheckable(True)
		self.btn1.toggle()
		self.btn1.clicked.connect(lambda:self.whichbtn(self.btn1) )
		self.btn1.clicked.connect(self.btnstate)
		layout.addWidget(self.btn1)
            
		self.btn2 = QPushButton('image')
		self.btn2.setIcon(QIcon(QPixmap("./images/python.png")))
		self.btn2.clicked.connect(lambda:self.whichbtn(self.btn2) )
		layout.addWidget(self.btn2)
		self.setLayout(layout) 

		self.btn3 = QPushButton("Disabled")
		self.btn3.setEnabled(False)
		layout.addWidget(self.btn3)
        
		self.btn4= QPushButton("&Download")
		self.btn4.setDefault(True)
		self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
		layout.addWidget(self.btn4)
		self.setWindowTitle("Button demo")

	def btnstate(self):
		if self.btn1.isChecked():
			print("button pressed" ) 
		else:
			print("button released" ) 

	def whichbtn(self,btn):
		print("clicked button is " + btn.text() ) 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	btnDemo = Form()
	btnDemo.show()
	sys.exit(app.exec_())


