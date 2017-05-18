# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5中表格头为自适应模式例子
  
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication , QTableWidgetItem, QHeaderView)

class Table(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("QTableWidget demo")
		self.resize(500,300);
		conLayout = QHBoxLayout()
		tableWidget= QTableWidget()
		tableWidget.setRowCount(4)
		tableWidget.setColumnCount(3)
		conLayout.addWidget(tableWidget )
		
		tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
		#tableWidget.setVerticalHeaderLabels(['行1','行2','行3','行4' ])        
		tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
				 
		newItem = QTableWidgetItem("张三")  
		tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		tableWidget.setItem(0, 2, newItem)   
		
		self.setLayout(conLayout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
