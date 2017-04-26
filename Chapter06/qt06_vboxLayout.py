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
        self.initUi()

    def initUi(self):
        vlayout = QVBoxLayout()
         # 局部布局添加部件（例如：按钮）
        vlayout.addWidget( QPushButton(str(1)))
        vlayout.addWidget( QPushButton(str(2)))
        vlayout.addWidget( QPushButton(str(3)))
        self.setLayout(vlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
