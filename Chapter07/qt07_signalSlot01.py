# -*- coding: utf-8 -*-

"""
    【简介】
    内置信号、自定义槽的演示程序


"""

import sys
from PyQt5.QtWidgets import QWidget,QPushButton, QApplication

class Winform(QWidget):
	def __init__(self):
		super(Winform, self).__init__()        
		self.setGeometry(200,300,350,50)
		self.setWindowTitle("内置信号、自定义槽的例子")
		
		self.btn = QPushButton("按钮文本",self)  
		self.btn.clicked.connect(self.changeBtnText)  
	
	def changeBtnText(self):  
		self.btn.setText("按钮内容和宽度改变了")  
		self.btn.setStyleSheet("QPushButton{max-width:200px; min-width:200px}")
	
if __name__ == '__main__':
    app = QApplication(sys.argv)
    qb = Winform()
    qb.show()
    sys.exit(app.exec_())
    
    
    
    
