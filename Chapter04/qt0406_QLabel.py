# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5 import QtCore  
from PyQt5.QtGui import QPixmap 
import sys  
    
class Absolute(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        l1=QLabel(self)
        l2=QLabel(self)
        l3=QLabel(self)
        l4=QLabel(self)
        l1.setText("Hello World")
        l4.setText("<A href='http://www.baidu.com'>Baidu</a>")
        l2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l4.setAlignment(QtCore.Qt.AlignRight)
        l3.setPixmap(QPixmap("./images/python.jpg"))
        
        vbox=QVBoxLayout()
        vbox.addWidget(l1)
        vbox.addStretch()
        vbox.addWidget(l2)
        vbox.addStretch()
        vbox.addWidget(l3)
        vbox.addStretch()
        vbox.addWidget(l4)
        
        l1.setOpenExternalLinks(True)
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        l4.setOpenExternalLinks( False )
        # 点击文本框绑定槽事件  
        l4.linkActivated.connect( link_clicked )
        
        # 划过文本框绑定槽事件       
        l2.linkHovered.connect( link_hovered )
        l1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel Demo")
        
def link_hovered():
    print( "hovering label2")
        
def link_clicked():
    print( "clicked label4" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    qb = Absolute()  
    qb.show()  
    sys.exit(app.exec_())