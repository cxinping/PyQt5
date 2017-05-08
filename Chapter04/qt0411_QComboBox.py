# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QComboBox 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboxDemo(QWidget):
	def __init__(self, parent=None):
		super(ComboxDemo, self).__init__(parent)
		self.setWindowTitle("combox 例子")        
		self.resize(300, 90)                       
		layout = QHBoxLayout()
		self.cb = QComboBox()
		self.cb.addItem("C")
		self.cb.addItem("C++")
		self.cb.addItems(["Java", "C#", "Python"])
		self.cb.currentIndexChanged.connect(self.selectionchange)
		layout.addWidget(self.cb)
		self.setLayout(layout)
                                    
	def selectionchange(self,i):
		print( "Items in the list are :" )
		for count in range(self.cb.count()):
			print( 'item'+str(count) + '='+ self.cb.itemText(count) )
			print( "Current index",i,"selection changed ",self.cb.currentText() )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = ComboxDemo()
	comboxDemo.show()
	sys.exit(app.exec_())
