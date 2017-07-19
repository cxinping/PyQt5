# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTabWidget 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
          
class TabDemo(QTabWidget):
	def __init__(self, parent=None):
		super(TabDemo, self).__init__(parent)   
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.addTab(self.tab1,"Tab 1")
		self.addTab(self.tab2,"Tab 2")
		self.addTab(self.tab3,"Tab 3")
		self.tab1UI()
		self.tab2UI()
		self.tab3UI()
		self.setWindowTitle("Tab 例子")
		
	def tab1UI(self):
		layout = QFormLayout()
		layout.addRow("姓名",QLineEdit())
		layout.addRow("地址",QLineEdit())
		self.setTabText(0,"联系方式")
		self.tab1.setLayout(layout)
		
	def tab2UI(self):
		layout = QFormLayout()
		sex = QHBoxLayout()
		sex.addWidget(QRadioButton("男"))    
		sex.addWidget(QRadioButton("女"))
		layout.addRow(QLabel("性别"),sex)
		layout.addRow("生日",QLineEdit())
		self.setTabText(1,"个人详细信息")
		self.tab2.setLayout(layout)
		
	def tab3UI(self):
		layout=QHBoxLayout()
		layout.addWidget(QLabel("科目"))
		layout.addWidget(QCheckBox("物理"))
		layout.addWidget(QCheckBox("高数"))
		self.setTabText(2,"教育程度")
		self.tab3.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = TabDemo()
	demo.show()
	sys.exit(app.exec_())
