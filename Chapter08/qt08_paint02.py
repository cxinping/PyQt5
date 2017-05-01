# -*- coding: utf-8 -*-
 
"""
    【简介】
    不规则窗体的实现
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import  QPixmap,   QPainter , QBitmap

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("不规则窗体的实现例子") 

		self.pix = QBitmap("./images/mask.png")
		self.resize(self.pix.size())
		self.setMask(self.pix)
         
	def paintEvent(self,event):
		painter = QPainter(self)
        #在指定区域直接绘制窗口背景
		painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap("./images/screen1.jpg"))
		#绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        #painter.drawPixmap(0,0,self.width(),self.height(),QPixmap("./images/screen1.jpg"))
        
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
