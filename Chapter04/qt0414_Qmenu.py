# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 Qmenu 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class menudemo(QMainWindow):
	def __init__(self, parent=None):
		super(menudemo, self).__init__(parent)
		layout = QHBoxLayout()
		bar = self.menuBar()
		file = bar.addMenu("File")
		file.addAction("New")
		save = QAction("Save",self)
		save.setShortcut("Ctrl+S")
		file.addAction(save)
		edit = file.addMenu("Edit")
		edit.addAction("copy")
		edit.addAction("paste")
		quit = QAction("Quit",self)
		file.addAction(quit)
		file.triggered[QAction].connect(self.processtrigger) 
		self.setLayout(layout)
		self.setWindowTitle("menu demo")
		
	def processtrigger(self,q):
		print( q.text()+" is triggered" )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = menudemo()
	ex.show()
	sys.exit(app.exec_())
