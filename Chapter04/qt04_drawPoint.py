# -*- coding: utf-8 -*-
 
"""
    【简介】
    在窗体中绘画点的例子
    
    
"""

import sys, math
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt 

class Drawing(QWidget):
	def __init__(self, parent=None):
		super(Drawing, self).__init__(parent)
		self.resize(300, 200)  
		self.setWindowTitle("在窗体中画点")         

	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		# 自定义画点方法
		self.drawPoints(qp)
		qp.end()
		
	def drawPoints(self,  qp):
		qp.setPen( Qt.red)
		size = self.size()
		
		for i in range(1000):
			# [-100, 100]两个周期的正弦函数图像
			x = 100 *(-1+2.0*i/1000)+ size.width()/2.0
			y = -50 * math.sin((x - size.width()/2.0)*math.pi/50) + size.height()/2.0
			qp.drawPoint(x, y)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo  = Drawing()
	demo.show()
	sys.exit(app.exec_())
