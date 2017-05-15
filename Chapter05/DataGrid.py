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
		self.prevButton = QPushButton("前一页")
		self.nextButton = QPushButton("下一页")
		switchPageButton = QPushButton("Go")
		switchPageLineEdit = QLineEdit()
		switchPageLineEdit.setFixedWidth(40)	
		
		switchPage =  QLabel("转到第")
		page = QLabel("页")
		operatorLayout.addWidget(self.prevButton)
		operatorLayout.addWidget(self.nextButton)
		operatorLayout.addWidget(switchPage)
		operatorLayout.addWidget(switchPageLineEdit)
		operatorLayout.addWidget(page)
		operatorLayout.addWidget(switchPageButton)
		operatorLayout.addWidget( QSplitter())
	
	    # 状态布局
		statusLayout =  QHBoxLayout()
		self.totalPageLabel =  QLabel()
		self.totalPageLabel.setFixedWidth(70)
		currentPageLabel =  QLabel()
		currentPageLabel.setFixedWidth(70)
		statusLayout.addWidget(self.totalPageLabel)
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
		self.queryModel = QSqlQueryModel(self);
		# 设置当前页
		self.currentPage = 1;
		# 得到总记录数
		self.totalRecrodCount = self.GetTotalRecordCount();
		# 得到总页数
		self.totalPage = self.GetPageCount();
		# 刷新状态
		self.UpdateStatus();
		# 设置总页数文本
		self.SetTotalPageLabel();
		# 记录查询
		#RecordQuery(0);
		# 设置模型
		self.tableView.setModel(self.queryModel)
		
		# 设置表格表头
		self.queryModel.setHeaderData(0,Qt.Horizontal,"编号"); 
		self.queryModel.setHeaderData(1,Qt.Horizontal,"姓名");
		self.queryModel.setHeaderData(2,Qt.Horizontal,"性别");
		self.queryModel.setHeaderData(3,Qt.Horizontal,"年龄");
		self.queryModel.setHeaderData(4,Qt.Horizontal,"院系");

	# 得到记录数	
	def GetTotalRecordCount(self):			
		self.queryModel.setQuery("select * from student");
		return self.queryModel.rowCount()
			
	# 得到页数		
	def GetPageCount(self):			
		if ( self.totalRecrodCount % self.PageRecordCount == 0 ) :
			return (self.totalRecrodCount / self.PageRecordCount)
		else :
			return (self.totalRecrodCount / self.PageRecordCount + 1)

	# 记录查询		
	def RecordQuery(self):	
		szQuery = ("select * from student limit %d,%d" % ( self.limitIndex , self.PageRecordCount ) )

		
	# 刷新状态		
	def UpdateStatus(self):				
		szCurrentText = ("当前第%d 1页" % self.currentPage )
		#self.currentPageLabel.setText(szCurrentText)
		#设置按钮是否可用
		if( self.currentPage == 1):
			self.prevButton.setEnabled( False )
			self.nextButton.setEnabled( True )
		elif  ( self.currentPage == self.totalPage ):
			self.prevButton.setEnabled( True )
			self.nextButton.setEnabled( False )
		else :
			self.prevButton.setEnabled( True )
			self.nextButton.setEnabled( True )

	# 设置总数页文本		
	def SetTotalPageLabel(self):	
		szPageCountText  = ("总共%d页" % self.totalPage )
		self.totalPageLabel.setText(szPageCountText)
			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = DataGrid()  
	example.show()   
	sys.exit(app.exec_())
