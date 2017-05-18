# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中单元格添加图片例子
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore  import *

class Table( QWidget ):
         
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget 例子")
		self.resize(500,300);
		conLayout = QHBoxLayout()
		self.tableWidget= QTableWidget()
		self.tableWidget.setRowCount(5)
		self.tableWidget.setColumnCount(4)
		conLayout.addWidget(self.tableWidget )
				 
		self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重', '显示图片'])  
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		                                		
		newItem = QTableWidgetItem("张三")    
		self.tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		self.tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		self.tableWidget.setItem(0, 2, newItem)   
		
		newItem = QTableWidgetItem(QIcon("./images/bao1.png"), "背包")
		self.tableWidget.setItem(0, 3, newItem ) 
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
