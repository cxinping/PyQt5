# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中Qlabel例子
   按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
  
'''

from PyQt5.QtWidgets import *
import sys  
    
class QlabelDemo(QDialog):  
    def __init__(self ):  
        super().__init__()
         
        self.setWindowTitle('Qlabel 例子')
        nameLb1 = QLabel('&Name', self)
        nameEd1 = QLineEdit( self )
        nameLb1.setBuddy(nameEd1)
        
        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit( self )
        nameLb2.setBuddy(nameEd2)
        
        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1,0,0)
        mainLayout.addWidget(nameEd1,0,1,1,2)
        
        mainLayout.addWidget(nameLb2,1,0)
        mainLayout.addWidget(nameEd2,1,1,1,2)
         
        mainLayout.addWidget(btnOk,2,1)
        mainLayout.addWidget(btnCancel,2,2) 
        
def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")
        
def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    labelDemo = QlabelDemo()  
    labelDemo.show()  
    sys.exit(app.exec_())
