# -*- coding: utf-8 -*- 

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout , QVBoxLayout , QApplication, QPushButton, QLineEdit ,QLabel , QSplitter ,  QTableView , QHeaderView )
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal,  Qt
from PyQt5.QtSql import QSqlDatabase , QSqlQuery, QSqlQueryModel

class DataGrid(QWidget):

	#OnPrevButtonClick = pyqtSignal()
	#OnNextButtonClick = pyqtSignal()
	#OnSwitchPageButtonClick = pyqtSignal()

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
		
		# 信号槽连接
		self.prevButton.clicked.connect(self.OnPrevButtonClick )		
		self.nextButton.clicked.connect(self.OnNextButtonClick )	
		self.switchPageButton.clicked.connect(self.OnSwitchPageButtonClick )	
		
		
	def CreateWindow(self):
		# 操作布局
		operatorLayout = QHBoxLayout()
		self.prevButton = QPushButton("前一页")
		self.nextButton = QPushButton("下一页")
		self.switchPageButton = QPushButton("Go")
		self.switchPageLineEdit = QLineEdit()
		self.switchPageLineEdit.setFixedWidth(40)	
		
		switchPage =  QLabel("转到第")
		page = QLabel("页")
		operatorLayout.addWidget(self.prevButton)
		operatorLayout.addWidget(self.nextButton)
		operatorLayout.addWidget(switchPage)
		operatorLayout.addWidget(self.switchPageLineEdit)
		operatorLayout.addWidget(page)
		operatorLayout.addWidget(self.switchPageButton)
		operatorLayout.addWidget( QSplitter())
	
	    # 状态布局
		statusLayout =  QHBoxLayout()
		self.totalPageLabel =  QLabel()
		self.totalPageLabel.setFixedWidth(70)
		self.currentPageLabel =  QLabel()
		self.currentPageLabel.setFixedWidth(70)
		statusLayout.addWidget(self.totalPageLabel)
		statusLayout.addWidget(self.currentPageLabel)
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
		self.RecordQuery(0);
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
	def RecordQuery(self, limitIndex ):	
		szQuery = ("select * from student limit %d,%d" % (  limitIndex , self.PageRecordCount ) )
		print('szQuery => ' + szQuery )
		self.queryModel.setQuery(szQuery)
		
	# 刷新状态		
	def UpdateStatus(self):				
		szCurrentText = ("当前第%d页" % self.currentPage )
		self.currentPageLabel.setText( szCurrentText )
        
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

	# 前一页按钮按下		
	def OnPrevButtonClick(self):	
		limitIndex = (self.currentPage - 2) * self.PageRecordCount
		self.RecordQuery( limitIndex) 
		self.currentPage -= 1 
		self.UpdateStatus() 

	# 后一页按钮按下	
	def OnNextButtonClick(self):	
		limitIndex =  self.currentPage * self.PageRecordCount
		self.RecordQuery( limitIndex) 
		self.currentPage+= 1
		self.UpdateStatus() 
		
	# 转到页按钮按下
	def OnSwitchPageButtonClick(self):			
		# 得到输入字符串
		szText = self.switchPageLineEdit.text()
		#数字正则表达式		
		pattern = re.compile(r'-?[0-9]*')
		match = pattern.match(szText)
		
		# 判断是否为数字
		if not match :
			QMessageBox.information(self, "提示", "请输入数字" )
			return
			
		# 是否为空
		if szText == '' :
			QMessageBox.information(this, "提示" , "请输入跳转页面" )
			return

		#得到页数
		pageIndex = int(szText)
		#判断是否有指定页
		if pageIndex > self.totalPage or pageIndex < 1 :
			QMessageBox.information(self, "提示", "没有指定的页面，请重新输入" )
			return
			
		#得到查询起始行号
		limitIndex = (pageIndex-1) * self.PageRecordCount			
			
		#记录查询
		self.RecordQuery(limitIndex);
		#设置当前页
		self.currentPage = pageIndex
		#刷新状态
		self.UpdateStatus();

			
if __name__ == '__main__':
	app = QApplication(sys.argv)
	# 创建窗口
	example = DataGrid()  
	# 显示窗口
	example.show()   
	sys.exit(app.exec_())
