# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中QRadio例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Radiodemo(QWidget):
	def __init__(self, parent=None):
		super(Radiodemo, self).__init__(parent)
		layout = QHBoxLayout()
		self.btn1 = QRadioButton("Button1")
		self.btn1.setChecked(True)
		self.btn1.toggled.connect(lambda:self.btnstate(self.btn1))
		layout.addWidget(self.btn1)
        
		self.btn2 = QRadioButton("Button2")
		self.btn2.toggled.connect(lambda:self.btnstate(self.btn2))
		layout.addWidget(self.btn2)
		self.setLayout(layout)
		self.setWindowTitle("RadioButton demo")
	
	def btnstate(self,btn):
		if btn.text()=="Button1":
			if btn.isChecked() == True:
				print( btn.text() + " is selected" )
			else:
				print( btn.text() + " is deselected" )
		
		if btn.text()=="Button2":
			if btn.isChecked()== True :
				print( btn.text() + " is selected" )
			else:
				print( btn.text() + " is deselected" )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	radioDemo = Radiodemo()
	radioDemo.show()
	sys.exit(app.exec_())
