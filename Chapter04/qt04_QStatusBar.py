# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QStatusBar 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StatusDemo(QMainWindow):
	def __init__(self, parent=None):
		super(StatusDemo, self).__init__(parent)
		bar = self.menuBar()
		file = bar.addMenu("File")
		file.addAction("show")
		file.triggered[QAction].connect(self.processTrigger)
		self.setCentralWidget(QTextEdit())
		self.statusBar= QStatusBar() 
		self.setWindowTitle("QStatusBar 例子")
		self.setStatusBar(self.statusBar)
	
	def processTrigger(self,q):
		if (q.text()=="show"):
			self.statusBar.showMessage(q.text()+" 菜单选项被点击了",5000)
	    
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = StatusDemo()
	demo.show()
	sys.exit(app.exec_())
