# -*- coding: utf-8 -*- 

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout , QVBoxLayout , QApplication, QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , QHeaderView )
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal,  Qt
from PyQt5.QtSql import QSqlDatabase , QSqlQuery, QSqlQueryModel

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
		self.tableView = QTableView()
		#tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		#tableView.verticalHeader().setResizeMode(QHeaderView.Stretch)
		#self.tableView.horizontalHeader().setStretchLastSection(True)
		#self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		# 创建界面
		mainLayout =  QVBoxLayout(self);
		mainLayout.addLayout(operatorLayout);
		mainLayout.addWidget(self.tableView);
		mainLayout.addLayout(statusLayout);
		self.setLayout(mainLayout)

	def SetTableView(self):		
		# 声明查询模型
		queryModel = QSqlQueryModel(self);
		# 设置当前页
		self.currentPage = 1;
		# 得到总记录数
		self.totalRecrodCount = self.GetTotalRecordCount();
		# 得到总页数
		#self.totalPage = GetPageCount();
		# 刷新状态
		#UpdateStatus();
		# 设置总页数文本
		#SetTotalPageLabel();
		# 记录查询
		#RecordQuery(0);
		# 设置模型
		self.tableView.setModel(queryModel)
		
		# 设置表格表头
		queryModel.setHeaderData(0,Qt.Horizontal,"编号"); 
		queryModel.setHeaderData(1,Qt.Horizontal,"姓名");
		queryModel.setHeaderData(2,Qt.Horizontal,"性别");
		queryModel.setHeaderData(3,Qt.Horizontal,"年龄");
		queryModel.setHeaderData(4,Qt.Horizontal,"院系");

	def GetTotalRecordCount(self):			
		if ( self.totalRecrodCount % self.PageRecordCount == 0 ) :
			return (self.totalRecrodCount / self.PageRecordCount)
		else :
			return (self.totalRecrodCount / self.PageRecordCount + 1)




			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = DataGrid()  
	example.show()   
	sys.exit(app.exec_())
