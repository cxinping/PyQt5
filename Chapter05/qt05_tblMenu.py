# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5的表格中支持右键菜单例子
    
  
'''

import sys
from PyQt5.QtWidgets import ( QMenu , QPushButton,  QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import  QObject, Qt 

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
		self.tableWidget.setColumnCount(3)
		conLayout.addWidget(self.tableWidget )
				
		self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重' ])  
		self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		
		newItem = QTableWidgetItem("张三")      
		self.tableWidget.setItem(0, 0, newItem)  
		  
		newItem = QTableWidgetItem("男")  
		self.tableWidget.setItem(0, 1, newItem)  
		  
		newItem = QTableWidgetItem("160")  
		self.tableWidget.setItem(0, 2, newItem)   
		#表格中第二行记录
		newItem = QTableWidgetItem("李四")      
		self.tableWidget.setItem(1, 0, newItem)  
		  
		newItem = QTableWidgetItem("女")  
		self.tableWidget.setItem(1, 1, newItem)  
		  
		newItem = QTableWidgetItem("170")  
		self.tableWidget.setItem(1, 2, newItem)   
		
		self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)######允许右键产生子菜单
		self.tableWidget.customContextMenuRequested.connect(self.generateMenu)   ####右键菜单
		self.setLayout(conLayout)
        
	def generateMenu(self,pos):
		#rint( pos)
		row_num = -1
		for i in self.tableWidget.selectionModel().selection().indexes():
			row_num = i.row()
		
		if row_num < 2 :
			menu = QMenu()
			item1 = menu.addAction(u"选项一")
			item2 = menu.addAction(u"选项二")
			item3 = menu.addAction(u"选项三" )
			action = menu.exec_(self.tableWidget.mapToGlobal(pos))
			if action == item1:
				print( '您选了选项一，当前行文字内容是：',self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text())

			elif action == item2:
				print( '您选了选项二，当前行文字内容是：',self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text() )

			elif action == item3:
				print( '您选了选项三，当前行文字内容是：', self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text() ,self.tableWidget.item(row_num,2).text() )
			else:
				return
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = Table()  
	example.show()   
	sys.exit(app.exec_())
