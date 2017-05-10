# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  Drag and Drop 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class combo(QComboBox):

	def __init__(self, title, parent):
		super(combo, self).__init__( parent)
		self.setAcceptDrops(True)
		
	def dragEnterEvent(self, e):
		print( e)
		if e.mimeData().hasText():
			e.accept()
		else:
			e.ignore() 

	def dropEvent(self, e):
		self.addItem(e.mimeData().text()) 
		
class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		lo=QFormLayout()
		lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
		edit = QLineEdit()
		edit.setDragEnabled(True)
		com = combo("Button", self)
		lo.addRow(edit,com)
		self.setLayout(lo)
		self.setWindowTitle('Simple drag & drop')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example() 
	ex.show()
	app.exec_() 
