# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QListView 例子       
  
'''

from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView, QMessageBox
from PyQt5.QtCore import QStringListModel  
import sys  

class ListViewDemo(QWidget):
	def __init__(self, parent=None):
		super(ListViewDemo, self).__init__(parent)
		self.setWindowTitle("QListView 例子")
		self.resize(300, 270)    
		layout = QVBoxLayout()
		
		listView = QListView()      
		slm = QStringListModel();
		self.qList = ['Item 1','Item 2','Item 3','Item 4' ]	
		slm.setStringList(self.qList)
		listView.setModel(slm )
		listView.clicked.connect(self.clicked)		
		layout.addWidget( listView )
		self.setLayout(layout) 		 

	def clicked(self, qModelIndex):
		QMessageBox.information(self, "QListView", "你选择了: "+ self.qList[qModelIndex.row()])
		
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = ListViewDemo()	
	win.show()	
	sys.exit(app.exec_())
