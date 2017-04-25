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
		self.resize(600, 400)
        
	def paintEvent(self,event):
		painter = QPainter(self)
		painter.drawPixmap(0,0,280,390,QPixmap(r"./images/dog.jpg"))
		painter.drawPixmap(300,0,280,390,QBitmap(r"./images/dog.jpg"))
         
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = Winform()
	form.show()
	sys.exit(app.exec_())
