# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery

def createDB():
	db =  QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/sports.db')
	if not db.open():
		QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
		QtGui.qApp.tr("Unable to establish a database connection. \n"
		"This example needs SQLite support. Please read "
		"the Qt SQL driver documentation for information "
		"how to build it.\n\n"
		"Click Cancel to exit."),
		QtGui.QMessageBox.Cancel)
		return False
	
	query = QSqlQuery()
	query.exec_("create table sportsmen(id int primary key, "
	"firstname varchar(20), lastname varchar(20))")
	query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
	query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
	query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
	query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
	query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
	return True

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	createDB() 
	sys.exit(app.exec_())
		
