# -*- coding: utf-8 -*-
 
"""
    【简介】
    使用paintEvent设置窗口背景图片
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import  QPixmap,   QPainter 

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("paintEvent设置背景图片") 
         
	def paintEvent(self,event):
		painter = QPainter(self)
		pixmap = QPixmap("./images/screen1.jpg")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
		painter.drawPixmap(self.rect(),pixmap)    
        
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
