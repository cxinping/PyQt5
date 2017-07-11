# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5中Absolute positioning(绝对定位)例子
  
'''

import sys  
from PyQt5.QtWidgets import QWidget, QLabel, QApplication  
      
class Example(QWidget):        
    def __init__(self):  
        super().__init__()            
        self.initUI()  
          
    def initUI(self):            
        lbl1 = QLabel('欢迎', self)  
        lbl1.move(15, 10)  
  
        lbl2 = QLabel('学习', self)  
        lbl2.move(35, 40)  
          
        lbl3 = QLabel('PyQt5 !', self)  
        lbl3.move(55, 70)          
          
        self.setGeometry(300, 300, 320, 120)  
        self.setWindowTitle('绝对位置布局例子')      
                                  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    demo = Example()  
    demo.show()
    sys.exit(app.exec_())  
