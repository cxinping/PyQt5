# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5中表格头为自适应模式例子
  
    作者：信平
    QQ： 759949947	
    Email: xpws2006@163.com   
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QDesktopWidget, QTableWidgetItem, QHeaderView)

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(500,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
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