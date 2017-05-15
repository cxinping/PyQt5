# -*- coding: utf-8 -*- 

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout , QVBoxLayout , QApplication, QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , QHeaderView )

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery

class DataGrid(QWidget):

	OnPrevButtonClick = pyqtSignal()
	OnNextButtonClick = pyqtSignal()
	OnSwitchPageButtonClick = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.setWindowTitle("分页查询例子")
		self.resize(600,300);		
		self.queryModel = None
		self.tableView = None		
		self.totalPageLabel = None
		self.currentPageLabel = None			
		self.switchPageLineEdit = None
		self.prevButton = None		
		self.nextButton = None
		self.switchPageButton = None				
		self.currentPage = 0
		self.totalPage = 0		
		self.totalRecrodCount = 0
		self.PageRecordCount  = 5			
	
		self.initUI()

	def initUI(self):
		# 创建窗口
		self.CreateWindow()
		# 设置表格
		self.SetTableView()
		
	def CreateWindow(self):
		# 操作布局
		operatorLayout = QHBoxLayout()
		prevButton = QPushButton("前一页")
		nextButton = QPushButton("下一页")
		switchPageButton = QPushButton("Go")
		switchPageLineEdit = QLineEdit()
		switchPageLineEdit.setFixedWidth(40)	
		
		switchPage =  QLabel("转到第")
		page = QLabel("页")
		operatorLayout.addWidget(prevButton)
		operatorLayout.addWidget(nextButton)
		operatorLayout.addWidget(switchPage)
		operatorLayout.addWidget(switchPageLineEdit)
		operatorLayout.addWidget(page)
		operatorLayout.addWidget(switchPageButton)
		operatorLayout.addWidget( QSplitter())
	
	    # 状态布局
		statusLayout =  QHBoxLayout()
		totalPageLabel =  QLabel()
		totalPageLabel.setFixedWidth(70)
		currentPageLabel =  QLabel()
		currentPageLabel.setFixedWidth(70)
		statusLayout.addWidget(totalPageLabel)
		statusLayout.addWidget(currentPageLabel)
		statusLayout.addWidget( QSplitter())	
		
		# 设置表格属性
		tableView = QTableView()
		#tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		#tableView.verticalHeader().setResizeMode(QHeaderView.Stretch)
		#self.tableView.horizontalHeader().setStretchLastSection(True)
		#self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		# 创建界面
		mainLayout =  QVBoxLayout(self);
		mainLayout.addLayout(operatorLayout);
		mainLayout.addWidget(tableView);
		mainLayout.addLayout(statusLayout);
		self.setLayout(mainLayout)

	def SetTableView(self):		
		pass
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = DataGrid()  
	example.show()   
	sys.exit(app.exec_())
