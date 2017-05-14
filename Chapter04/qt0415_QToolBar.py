# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QToolBar 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolBarDemo( QMainWindow ):

	def __init__(self, parent=None):
		super(ToolBarDemo, self).__init__(parent)
		self.setWindowTitle("toolbar 例子")		
		self.resize(300, 200)
		
		layout = QVBoxLayout()
		tb = self.addToolBar("File")
		new = QAction(QIcon("./images/new.png"),"new",self)
		tb.addAction(new)
		open = QAction(QIcon("./images/open.png"),"open",self)
		tb.addAction(open)
		save = QAction(QIcon("./images/save.png"),"save",self)
		tb.addAction(save)
		tb.actionTriggered[QAction].connect(self.toolbtnpressed)
		self.setLayout(layout)
           	
	def toolbtnpressed(self,a):
		print("pressed tool button is",a.text() )
           
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = ToolBarDemo()
	demo.show()
	sys.exit(app.exec_())
