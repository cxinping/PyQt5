# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QListView 例子       
  
'''

from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView
from PyQt5.QtCore import QStringListModel  
import sys  

class ListViewDemo(QWidget):
	def __init__(self, parent=None):
		super(ListViewDemo, self).__init__(parent)
		self.setWindowTitle("QListView 例子")
		self.resize(300, 270)    
		layout = QVBoxLayout()
		
		self.listView = QListView()      
		self.slm = QStringListModel();
		qList = ['a','b','c']	
		self.slm.setStringList(qList)
		self.listView.setModel(self.slm )
		layout.addWidget( self.listView )
		self.setLayout(layout) 		 
		
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = ListViewDemo()	
	win.show()	
	sys.exit(app.exec_())
