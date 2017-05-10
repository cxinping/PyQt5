# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QStackedWidget 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class stackedExample(QWidget):
	def __init__(self):
		super(stackedExample, self).__init__()
		self.setGeometry(300, 50, 10,10)
		self.setWindowTitle('StackedWidget demo')
		
		self.leftlist = QListWidget ()
		self.leftlist.insertItem (0, 'Contact' )
		self.leftlist.insertItem (1, 'Personal' )
		self.leftlist.insertItem (2, 'Educational' )
		self.stack1= QWidget()
		self.stack2= QWidget()
		self.stack3= QWidget()
		self.stack1UI()
		self.stack2UI()
		self.stack3UI()
		self.Stack = QStackedWidget (self)
		self.Stack.addWidget (self.stack1)
		self.Stack.addWidget (self.stack2)
		self.Stack.addWidget (self.stack3)
		hbox = QHBoxLayout(self)
		hbox.addWidget(self.leftlist)
		hbox.addWidget(self.Stack)
		self.setLayout(hbox)
		self.leftlist.currentRowChanged.connect(self.display)

	def stack1UI(self):
		layout=QFormLayout()
		layout.addRow("Name",QLineEdit())
		layout.addRow("Address",QLineEdit())
		#self.setTabText(0,"Contact Details")
		self.stack1.setLayout(layout)

	def stack2UI(self):
		layout=QFormLayout()
		sex=QHBoxLayout()
		sex.addWidget(QRadioButton("Male"))
		sex.addWidget(QRadioButton("Female"))
		layout.addRow(QLabel("Sex"),sex)
		layout.addRow("Date of Birth",QLineEdit())

		self.stack2.setLayout(layout)

	def stack3UI(self):
		layout=QHBoxLayout()
		layout.addWidget(QLabel("subjects"))
		layout.addWidget(QCheckBox("Physics"))
		layout.addWidget(QCheckBox("Maths"))
		self.stack3.setLayout(layout)
	
	def display(self,i):
		self.Stack.setCurrentIndex(i)
	
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = stackedExample()
	demo.show()
	sys.exit(app.exec_())
