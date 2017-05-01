# -*- coding: utf-8 -*-
 
"""
    【简介】
     嵌套布局
    
    
"""

from PyQt5.QtWidgets import *
import sys   
 
class MyWindow(QWidget):  

	def __init__(self):  
		super().__init__()
		self.setWindowTitle('嵌套布局示例')
		self.resize(700, 200)
        
        # 全局部件（注意参数 self），用于"承载"全局布局
		wwg = QWidget(self)
        
         # 全局布局（注意参数 wwg）
		wl = QHBoxLayout(wwg)
		hlayout =  QHBoxLayout()
		vlayout =  QVBoxLayout()
		glayout = QGridLayout()
		formlayout =  QFormLayout()
        
         # 局部布局添加部件（例如：按钮）
		hlayout.addWidget( QPushButton(str(1)) )
		hlayout.addWidget( QPushButton(str(2)) )
		vlayout.addWidget( QPushButton(str(3)) )
		vlayout.addWidget( QPushButton(str(4)) )
		glayout.addWidget( QPushButton(str(5)) , 0, 0 )
		glayout.addWidget( QPushButton(str(6)) , 0, 1 )
		glayout.addWidget( QPushButton(str(7)) , 1, 0)
		glayout.addWidget( QPushButton(str(8)) , 1, 1)
		formlayout.addWidget( QPushButton(str(9))  )
		formlayout.addWidget( QPushButton(str(10)) )
		formlayout.addWidget( QPushButton(str(11)) )
		formlayout.addWidget( QPushButton(str(12)) )
        
        # 这里向局部布局内添加部件,将他加到全局布局
		wl.addLayout(hlayout)  
		wl.addLayout(vlayout)
		wl.addLayout(glayout)
		wl.addLayout(formlayout)       

if __name__=="__main__":    
 
	app = QApplication(sys.argv)    
	win = MyWindow()  
	win.show()  
	sys.exit(app.exec_())
    
