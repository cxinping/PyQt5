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
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/database.db')
    
	if not db.open():
		QMessageBox.critical(None,  ("无法打开数据库"),
		( "无法建立到数据库的连接,这个例子需要SQLite 支持，请检查数据库配置。\n\n"
          "点击取消按钮退出应用。"),
			QMessageBox.Cancel )
		return False
	
	query = QSqlQuery()
	query.exec_("create table people(id int primary key, "
	"name varchar(20), address varchar(30))")
	query.exec_("insert into people values(1, 'zhangsan1', 'BeiJing')")
	query.exec_("insert into people values(2, 'lisi1', 'TianJing')")
	query.exec_("insert into people values(3, 'wangwu1', 'HenNan')")
	query.exec_("insert into people values(4, 'lisi2', 'HeBei')")
	query.exec_("insert into people values(5, 'wangwu2', 'shanghai')")
	return True

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	createDB() 
	sys.exit(app.exec_())
		
