# -*- coding: utf-8 -*-
 
"""
    【简介】
    水平布局管理例子
        
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton
from PyQt5.QtCore import Qt 

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("水平布局管理例子") 
		self.resize(800, 200)
		
		# 水平布局按照从左到右的顺序进行添加按钮部件。
		hlayout = QHBoxLayout()  
     
		#水平居左 垂直居上		
		hlayout.addWidget( QPushButton(str(1)) , 0 , Qt.AlignLeft | Qt.AlignTop)
		hlayout.addWidget( QPushButton(str(2)) , 0 , Qt.AlignLeft | Qt.AlignTop)
		hlayout.addWidget( QPushButton(str(3)))
		#水平居左 垂直居下
		hlayout.addWidget( QPushButton(str(4)) , 0 , Qt.AlignLeft | Qt.AlignBottom )        
		hlayout.addWidget( QPushButton(str(5)), 0 , Qt.AlignLeft | Qt.AlignBottom)    
      
		
		
		self.setLayout(hlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
