# -*- coding: utf-8 -*-
 
"""
    【简介】
    不规则的，可以拖动的窗体实现例子
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import  QPixmap,   QPainter  ,  QCursor , QBitmap
from PyQt5.QtCore import Qt 

class ShapeWidget(QWidget):  
	def __init__(self,parent=None):  
		super(ShapeWidget,self).__init__(parent)
		self.setWindowTitle("不规则的，可以拖动的窗体实现例子") 
		self.mypix()	

    # 显示不规则 pic
	def mypix(self):
		self.pix = QBitmap( "./images/mask.png" )
		self.resize(self.pix.size())       
		self.setMask(self.pix)
		print( self.pix.size())
		self.dragPosition = None

	# 重定义鼠标按下响应函数mousePressEvent(QMouseEvent)和鼠标移动响应函数mouseMoveEvent(QMouseEvent)，使不规则窗体能响应鼠标事件，随意拖动。
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.m_drag=True
			self.m_DragPosition=event.globalPos()-self.pos()
			event.accept()
			self.setCursor(QCursor(Qt.OpenHandCursor))
		if event.button()==Qt.RightButton:  
			self.close()  
			
	def mouseMoveEvent(self, QMouseEvent):
		if Qt.LeftButton and self.m_drag:
		    # 当左键移动窗体修改偏移值
			self.move(QMouseEvent.globalPos()- self.m_DragPosition )
			QMouseEvent.accept()
	
	def mouseReleaseEvent(self, QMouseEvent):
		self.m_drag=False
		self.setCursor(QCursor(Qt.ArrowCursor))
    
    #一般 paintEvent 在窗体首次绘制加载， 要重新加载paintEvent 需要重新加载窗口使用 self.update() or  self.repaint()    
	def paintEvent(self, event):
		painter = QPainter(self)
		painter.drawPixmap(0,0,self.width(),self.height(),QPixmap("./images/boy.png"))
			
if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=ShapeWidget()
    form.show()
    app.exec_()
