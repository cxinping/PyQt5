# -*- coding: utf-8 -*-
 
"""
    【简介】
    不规则窗体的动画实现
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import  QPixmap,   QPainter ,  QCursor 
from PyQt5.QtCore import Qt, QTimer

class ShapeWidget(QWidget):  
	def __init__(self,parent=None):  
		super(ShapeWidget,self).__init__(parent)
		self.i = 1
		self.mypix()
		self.timer = QTimer()
		self.timer.setInterval(500)  # 500毫秒
		self.timer.timeout.connect(self.timeChange)   
		self.timer.start()

    # 显示不规则 pic
	def mypix(self):
		self.update()
		if self.i == 5:
			self.i = 1
		self.mypic = {1: './images/left.png', 2: "./images/up.png", 3: './images/right.png', 4: './images/down.png'}
		self.pix = QPixmap(self.mypic[self.i], "0", Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)   
		self.resize(self.pix.size())
		self.setMask(self.pix.mask())  
		self.dragPosition = None

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.m_drag=True
			self.m_DragPosition=event.globalPos()-self.pos()
			event.accept()
			self.setCursor(QCursor(Qt.OpenHandCursor))

	def mouseMoveEvent(self, QMouseEvent):
		if Qt.LeftButton and self.m_drag:
			self.move(QMouseEvent.globalPos()- self.m_DragPosition )
			QMouseEvent.accept()
	
	def mouseReleaseEvent(self, QMouseEvent):
		self.m_drag=False
		self.setCursor(QCursor(Qt.ArrowCursor))
        
	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(0, 0, self.pix.width(),self.pix.height(),self.pix)
    
	# 鼠标双击事件
	def mouseDoubleClickEvent(self, event):
		if event.button() == 1:
			self.i += 1
			self.mypix()

    # 每500毫秒修改paint
	def timeChange(self):
		self.i += 1
		self.mypix()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	form = ShapeWidget()
	form.show()
	sys.exit(app.exec_())
