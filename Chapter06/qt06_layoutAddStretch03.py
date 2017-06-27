# -*- coding: utf-8 -*-
 
"""
    【简介】
    水平布局管理例子
        
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("水平布局管理例子") 
		self.resize(800, 50)
		
		# 水平布局按照从左到右的顺序进行添加按钮部件。
		hlayout = QHBoxLayout()  
       				
		hlayout.addWidget( QPushButton(str(1)) )
		hlayout.addWidget( QPushButton(str(2)) )
		hlayout.addWidget( QPushButton(str(3)))
		hlayout.addWidget( QPushButton(str(4)) )        
		hlayout.addWidget( QPushButton(str(5)))    
        # 添加伸缩控件		
		hlayout.addStretch(0)
								
		#设置间距
		#hlayout.setSpacing( 10 )	
		
		
		self.setLayout(hlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
