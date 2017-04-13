# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5中Qlabel例子
   按住 Alt + N , Alt + P , Alt + O , Alt + C 切换组件控件
  
'''
from PyQt5.QtWidgets import *
import sys  
    
class QlabelDemo(QDialog):  
    def __init__(self ):  
        super().__init__()
         
        self.setWindowTitle('Find Cell')
        lblFind1=QLabel('&Name')
        editFind1=QLineEdit()
        lblFind1.setBuddy(editFind1)
        
        lblFind2=QLabel('&Password')
        editFind2=QLineEdit()
        lblFind2.setBuddy(editFind2)
        
        btnOk= QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')
        mainLayout= QGridLayout(self)
        mainLayout.addWidget(lblFind1,0,0)
        mainLayout.addWidget(editFind1,0,1,1,2)
        
        mainLayout.addWidget(lblFind2,1,0)
        mainLayout.addWidget(editFind2,1,1,1,2)
         
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