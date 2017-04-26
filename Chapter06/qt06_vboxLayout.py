# -*- coding: utf-8 -*-
 
"""
    【简介】
    垂直布局管理例子
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QVBoxLayout , QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("垂直布局管理例子") 
		self.resize(330, 150)  
        # 垂直布局按照从上到下的顺序进行添加按钮部件。
		vlayout = QVBoxLayout()
		vlayout.addWidget( QPushButton(str(1)))
		vlayout.addWidget( QPushButton(str(2)))
		vlayout.addWidget( QPushButton(str(3)))
		vlayout.addWidget( QPushButton(str(4)))
		vlayout.addWidget( QPushButton(str(5)))
		self.setLayout(vlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
