# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery , QSqlDatabase , QSqlTableModel
from PyQt5.QtCore import Qt 

def initializeModel(model):
	model.setTable('sportsmen')
	model.setEditStrategy( QSqlTableModel.OnFieldChange)
	model.select()
	model.setHeaderData(0, Qt.Horizontal, "ID")
	model.setHeaderData(1, Qt.Horizontal, "First name")
	model.setHeaderData(2, Qt.Horizontal, "Last name")
	
def createView(title, model):
	view =  QTableView()
	view.setModel(model)
	view.setWindowTitle(title)
	return view
	
def addrow():
	print( model.rowCount() )
	ret = model.insertRows( model.rowCount(), 1 )
	print( ret )

def findrow(i):
	delrow= i.row()
	print('del row=%s' % str(delrow) )

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/sports.db')
	model = QSqlTableModel()
	delrow = -1
	initializeModel(model)
	view1 = createView("Table Model (View 1)", model) 
	view1.clicked.connect(findrow)
	
	dlg= QDialog()
	layout = QVBoxLayout()
	layout.addWidget(view1)
	button =  QPushButton("Add a row")
	button.clicked.connect(addrow)
	layout.addWidget(button)
    
	btn1 =  QPushButton("del a row")
	btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
	layout.addWidget(btn1)
	dlg.setLayout(layout)
	dlg.setWindowTitle("Database Demo")
	dlg.show()
	sys.exit(app.exec_())

	
	
	
