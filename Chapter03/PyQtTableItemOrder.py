# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5中单元格排序
  
    作者：信平
    QQ： 759949947	
    Email: xpws2006@163.com   
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
from PyQt5.QtGui import QBrush,  QColor ,  QFont 
import PyQt5.QtCore as QtCore

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(400,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
          
        newItem = QTableWidgetItem("张三")  
        tableWidget.setItem(0, 0, newItem)  
                 
        newItem = QTableWidgetItem("男")  
        tableWidget.setItem(0, 1, newItem)  
          
        newItem = QTableWidgetItem("160") 
        tableWidget.setItem(0, 2, newItem)   
      
        newItem = QTableWidgetItem("李四")  
        tableWidget.setItem(1, 0, newItem)  
                 
        newItem = QTableWidgetItem("女")  
        tableWidget.setItem(1, 1, newItem)  
          
        newItem = QTableWidgetItem("155") 
        tableWidget.setItem(1, 2, newItem)      
       
        newItem = QTableWidgetItem("王五")  
        tableWidget.setItem(2, 0, newItem)  
                 
        newItem = QTableWidgetItem("男")  
        tableWidget.setItem(2, 1, newItem)  
          
        newItem = QTableWidgetItem("170") 
        tableWidget.setItem(2, 2, newItem)        
        
   
        # QtCore.Qt.DescendingOrder 降序
        # QtCore.Qt.AscendingOrder 升序
        tableWidget.sortItems(2,  QtCore.Qt.DescendingOrder )
        
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
