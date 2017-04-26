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
        self.initUi()

    def initUi(self):
        hlayout = QHBoxLayout()
         # 局部布局添加部件（例如：按钮）
        hlayout.addWidget( QPushButton(str(1)))
        hlayout.addWidget( QPushButton(str(2)))
        hlayout.addWidget( QPushButton(str(3)))
        self.setLayout(hlayout)   
  
if __name__ == "__main__":  
		app = QApplication(sys.argv) 
		form = Winform()
		form.show()
		sys.exit(app.exec_())
