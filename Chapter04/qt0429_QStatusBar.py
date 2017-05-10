# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QStatusBar 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class statusdemo(QMainWindow):
	def __init__(self, parent=None):
		super(statusdemo, self).__init__(parent)
		bar=self.menuBar()
		file=bar.addMenu("File")
		file.addAction("show")
		file.addAction("add")
		file.addAction("remove")
		file.triggered[QAction].connect(self.processtrigger)
		self.setCentralWidget(QTextEdit())
		self.statusBar= QStatusBar() 
		self.b=QPushButton("click here")
		self.setWindowTitle("QStatusBar Example")
		self.setStatusBar(self.statusBar)
	
	def processtrigger(self,q):
		if (q.text()=="show"):
			self.statusBar.showMessage(q.text()+" is clicked",2000)
		if q.text()=="add":
			self.statusBar.addWidget(self.b)
		if q.text()=="remove":
			self.statusBar.removeWidget(self.b) 
			self.statusBar.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = statusdemo()
	ex.show()
	sys.exit(app.exec_())
