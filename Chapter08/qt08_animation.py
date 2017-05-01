# -*- coding: utf-8 -*-

"""
    【简介】
    动画的效果改变窗体大小
    
    
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class ani(QWidget):
    def __init__(self):
        super(ani, self).__init__()
        self.OrigHeight = 50
        self.ChangeHeight = 150
        # 在X=500， Y=400 ， Length=150 ,   Height=50
        self.setGeometry(QRect(500, 400, 150, self.OrigHeight)) 
        self.btn = QPushButton( '展开', self)
        self.btn.setGeometry(10, 10, 60, 35)
        self.machine = QStateMachine()
        self.btn.clicked.connect(self.change)         

    # 动画效果修改窗体大小
    def change(self):
        CurrentHeight = self.height()
        if self.OrigHeight == CurrentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText( '收缩')
        else:
            startHeight = self.ChangeHeight
            endHeight = self.OrigHeight
            self.btn.setText( '展开')
            
        self.animation = QPropertyAnimation(self,   b'geometry' )        
        self.animation.setDuration(800)
        self.animation.setStartValue(QRect(500, 400, 150, startHeight))
        self.animation.setEndValue(QRect(500, 400, 150, endHeight))
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ani()
    window.show()
    sys.exit(app.exec_())
