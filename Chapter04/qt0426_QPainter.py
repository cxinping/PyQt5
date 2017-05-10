# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  涂刷例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 

class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
	def initUI(self): 
		self.text = "hello world"
		self.setGeometry(100,100, 400,300)
		self.setWindowTitle('Draw Demo')
		self.show()
		
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		qp.setPen(QColor(Qt.red))
		qp.setFont(QFont('Arial', 20))
		qp.drawText(10,50, "hello Python")
		qp.setPen(QColor(Qt.blue))
		qp.drawLine(10,100,100,100)
		qp.drawRect(10,150,150,100)
		qp.setPen(QColor(Qt.yellow))
		qp.drawEllipse(100,50,100,50)
		qp.drawPixmap(220,10,QPixmap("./images/python.png"))
		qp.fillRect(200,175,150,100,QBrush(Qt.SolidPattern))
		qp.end()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example() 
	sys.exit(app.exec_())	
