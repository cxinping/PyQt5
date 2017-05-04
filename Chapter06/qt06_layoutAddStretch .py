2# -*- coding: utf-8 -*-

'''
    【简介】
	 布局中用到的addStretch函数例子
    
'''

from PyQt5.QtWidgets import QApplication ,QWidget, QVBoxLayout , QHBoxLayout  ,QPushButton
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
            
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)      
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')
        
        hbox = QHBoxLayout()
        # 设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget( btn1 )
        # 设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget( btn2 )
        # 设置伸缩量为1
        hbox.addStretch(1)
        hbox.addWidget( btn3 )
        # 设置伸缩量为1
        hbox.addStretch(1 )        

        self.setLayout(hbox)
        self.setWindowTitle("addStretch 例子")
                 
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())


