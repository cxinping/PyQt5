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
				
		# 水平布局按照从左到右的顺序进行添加按钮部件。
		hlayout = QHBoxLayout()  
        		
		hlayout.addWidget( QPushButton(str(1)) )
		hlayout.addWidget( QPushButton(str(2)) )
		hlayout.addWidget( QPushButton(str(3)))
		hlayout.addWidget( QPushButton(str(4))  )        
		hlayout.addWidget( QPushButton(str(5)))    
        		
		#设置控件间的间距
		hlayout.setSpacing( 0 )	
		self.setLayout(hlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
