# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中单元格的宽度和高度例子

    作者：信平
    QQ： 759949947	
    Email: xpws2006@163.com   
  
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(400,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
          
        newItem = QTableWidgetItem("张三")  
        tableWidget.setItem(0, 0, newItem)  
        
        tableWidget.setColumnWidth(1,150)  #将第2列的单元格，设置成150宽度
        tableWidget.setRowHeight(1,120)      #将第2行的单元格，设置成120的高度

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
