# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTabWidget 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class tabdemo(QTabWidget):
	def __init__(self, parent=None):
		super(tabdemo, self).__init__(parent)
		self.tab1  = QWidget()
		self.tab2  = QWidget()
		self.tab3  = QWidget()
		self.addTab(self.tab1,"Tab 1")
		self.addTab(self.tab2,"Tab 2")
		self.addTab(self.tab3,"Tab 3")
		self.tab1UI()
		self.tab2UI()
		self.tab3UI()
		self.setWindowTitle("tab demo")
		
	def tab1UI(self):
		layout=QFormLayout()
		layout.addRow("Name",QLineEdit())
		layout.addRow("Address",QLineEdit())
		self.setTabText(0,"Contact Details")
		self.tab1.setLayout(layout)
		
	def tab2UI(self):
		layout=QFormLayout()
		sex=QHBoxLayout()
		sex.addWidget(QRadioButton("Male")) 

		sex.addWidget(QRadioButton("Female"))
		layout.addRow(QLabel("Sex"),sex)
		layout.addRow("Date of Birth",QLineEdit())
		self.setTabText(1,"Personal Details")
		self.tab2.setLayout(layout)
		
	def tab3UI(self):
		layout=QHBoxLayout()
		layout.addWidget(QLabel("subjects"))
		layout.addWidget(QCheckBox("Physics"))
		layout.addWidget(QCheckBox("Maths"))
		self.setTabText(2,"Education Details")
		self.tab3.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = tabdemo()
	ex.show()
	sys.exit(app.exec_())
