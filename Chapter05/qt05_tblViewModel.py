# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5中QTableView表格视图控件的例子
   
  
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Table(QWidget):

	def __init__(self, arg=None):
		super(Table, self).__init__(arg)
		self.setWindowTitle("QTableView表格视图控件的例子") 		
		self.resize(500,300);
		self.model=QStandardItemModel(4,4);
		self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])
		
		for row in range(4):
			for column in range(4):
				item = QStandardItem("row %s, column %s"%(row,column))
				self.model.setItem(row, column, item)
		
		self.tableView=QTableView()
		self.tableView.setModel(self.model)
		#下面代码让表格100填满窗口
		#self.tableView.horizontalHeader().setStretchLastSection(True)
		#self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		dlgLayout=QVBoxLayout();
		dlgLayout.addWidget(self.tableView)
		self.setLayout(dlgLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)	
	table = Table()
	table.show()
	sys.exit(app.exec_())
