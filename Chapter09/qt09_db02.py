# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlTableModel
from PyQt5.QtCore import Qt 

def initializeModel(model):
	model.setTable('people')
	model.setEditStrategy( QSqlTableModel.OnFieldChange)
	model.select()
	model.setHeaderData(0, Qt.Horizontal, "ID")
	model.setHeaderData(1, Qt.Horizontal, "name")
	model.setHeaderData(2, Qt.Horizontal, "address")
	
def createView(title, model):
	view =  QTableView()
	view.setModel(model)
	view.setWindowTitle(title)
	return view
	
def addrow():
	ret = model.insertRows( model.rowCount(), 1 )
	print( 'insertRows=%s' %str(ret) )

def findrow(i):
	delrow= i.row()
	print('del row=%s' % str(delrow) )

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/database.db')
	model = QSqlTableModel()
	delrow = -1
	initializeModel(model)
	view1 = createView("Table Model (View 1)", model) 
	view1.clicked.connect(findrow)
	
	dlg = QDialog()
	layout = QVBoxLayout()
	layout.addWidget(view1)
	addBtn = QPushButton("添加一行")
	addBtn.clicked.connect(addrow)
	layout.addWidget(addBtn)
    
	delBtn = QPushButton("删除一行")
	delBtn.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
	layout.addWidget(delBtn)
	dlg.setLayout(layout)
	dlg.setWindowTitle("Database 例子")
	dlg.resize(430, 450)
	dlg.show()
	sys.exit(app.exec_())

	
	
	
