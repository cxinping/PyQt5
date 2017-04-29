# -*- coding: utf-8 -*-
 
"""
    【简介】
    在窗体中绘画出文字的例子
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import QPainter ,QColor ,QFont
from PyQt5.QtCore import Qt 

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("在窗体中绘画出文字") 
		self.text = '欢迎学习 PyQt5'
         
	def paintEvent(self,event):
		painter = QPainter(self)
     
		painter.begin(self)
        #自定义的绘画方法
		self.drawText(event, painter)
		painter.end()

	def drawText(self, event, qp):
        #设置笔的颜色
		qp.setPen( QColor(168, 34, 3) )
        #设置字体
		qp.setFont( QFont('SimSun', 20))
        #画出文本
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)
		
		
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
