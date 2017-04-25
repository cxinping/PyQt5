# -*- coding: utf-8 -*-
 
"""
    【简介】
    不规则窗体的实现
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget 
from PyQt5.QtGui import  QPixmap,   QPainter 

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("不规则窗体的实现例子") 
		#self.resize(650, 1000)
		#pixmap = QPixmap(r"./images/left.png")                
		#self.resize(pixmap.width(),pixmap.height())
        
	def paintEvent(self,event):
		pixmap = QPixmap(r"./images/dog2.jpg")        
		painter = QPainter(self)
        
		#painter.drawPixmap(0,0,pixmap.width(),pixmap.height(),pixmap)
		
		#print(pixmap.width()) 
		#print(pixmap.height()) 
		print('初始化绘制图形-paintEvent')

	def resizeEvent(self, QResizeEvent) :
		pixmap = QPixmap(r"./images/left.png")        
		self.setMask( pixmap.mask() );
		print('改变窗体时绘制图形-resizeEvent')
		#print( pixmap)
		
        
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = Winform()
	form.show()
	sys.exit(app.exec_())
