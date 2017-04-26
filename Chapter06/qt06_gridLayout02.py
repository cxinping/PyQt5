# -*- coding: utf-8 -*-
 
"""
    【简介】
    网格布局管理例子
    
    
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,     QTextEdit, QGridLayout, QApplication)  
    
class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.initUI()

	def initUI(self):            
		title = QLabel('标题')  
		author = QLabel('提交人')  
		review = QLabel('申告内容')  
 
		titleEdit = QLineEdit()  
		authorEdit = QLineEdit()  
		reviewEdit = QTextEdit()  
 
		grid = QGridLayout()  
		grid.setSpacing(10)  
 
		grid.addWidget(title, 1, 0)  
		grid.addWidget(titleEdit, 1, 1)  
  
		grid.addWidget(author, 2, 0)  
		grid.addWidget(authorEdit, 2, 1)  
  
		grid.addWidget(review, 3, 0)  
		grid.addWidget(reviewEdit, 3, 1, 5, 1)  
          
		self.setLayout(grid)   
          
		self.setGeometry(300, 300, 350, 300)  
		self.setWindowTitle('故障申告')
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
