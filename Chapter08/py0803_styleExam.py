# -*- coding: utf-8 -*-

'''
    【简介】
	 按钮和Label添加背景图片
    
'''

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout , QPushButton
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
        
        #1        
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image: url(./images/python.jpg);}")
        label1.setFixedWidth(476)
        label1.setFixedHeight(259)
        
        #2
        btn1 = QPushButton(self )  
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(48, 48)
        btn1.setMinimumSize(48, 48)
        style = '''
                    #btn1{
                        border-radius: 4px;
                        background-image: url('./images/add.png');
                        }
                    #btn1:Pressed{
                        background-image: url('./images/addhover.png');
                        }
                '''
        btn1.setStyleSheet(style)
        
        #3
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(btn1)
      
        self.setLayout(vbox)
        self.setWindowTitle("按钮和Label添加背景图片例子")
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())

