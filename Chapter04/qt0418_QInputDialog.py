# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QInputDialog 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Inputdialogdemo(QWidget):
	def __init__(self, parent=None):
		super(Inputdialogdemo, self).__init__(parent)
		layout = QFormLayout()
		self.btn=QPushButton("Choose from list")
		self.btn.clicked.connect(self.getItem)
		self.le=QLineEdit()
		layout.addRow(self.btn,self.le)
		self.btn1=QPushButton("get name")
		self.btn1.clicked.connect(self.gettext)
		self.le1=QLineEdit()
		layout.addRow(self.btn1,self.le1)
		self.btn2=QPushButton("Enter an integer")
		self.btn2.clicked.connect(self.getint)
		self.le2=QLineEdit()
		layout.addRow(self.btn2,self.le2)
		self.setLayout(layout)
		self.setWindowTitle("Input Dialog demo")
		
	def getItem(self):
		items = ("C", "C++", "Java", "Python")
		item, ok = QInputDialog.getItem(self, "select input dialog",
		"list of languages", items, 0, False)
		if ok and item:
			self.le.setText(item)
	
	def gettext(self):	
		text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
		if ok:
			self.le1.setText(str(text)) 

	def getint(self):
		num,ok=QInputDialog.getInt(self,"integer input dualog","enter a number")
		if ok:
			self.le2.setText(str(num))
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Inputdialogdemo()
	demo.show()
	sys.exit(app.exec_())
