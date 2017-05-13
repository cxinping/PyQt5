# -*- coding: utf-8 -*-
 
"""
    【简介】
    绘图中QPen 的例子 ,绘制使用不同样式的6条线
    
    
"""

import sys 
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 

class Drawing(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):   
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle('钢笔样式例子')        

	def paintEvent(self, e): 
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)

		qp.setPen(pen)
		qp.drawLine(20, 40, 250, 40)

		pen.setStyle(Qt.DashLine)
		qp.setPen(pen)
		qp.drawLine(20, 80, 250, 80)

		pen.setStyle(Qt.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 120, 250, 120)

		pen.setStyle(Qt.DotLine)
		qp.setPen(pen)
		qp.drawLine(20, 160, 250, 160)

		pen.setStyle(Qt.DashDotDotLine)
		qp.setPen(pen)
		qp.drawLine(20, 200, 250, 200)

		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])
		qp.setPen(pen)
		qp.drawLine(20, 240, 250, 240)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Drawing()
	demo.show()
	sys.exit(app.exec_())
