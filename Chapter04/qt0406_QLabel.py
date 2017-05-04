# -*- coding: utf-8 -*-


'''
    【简介】
	PyQT5中Qlabel例子
     
'''

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap ,QPalette
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        
        #1
        label1.setText("这是一个文本标签。")
        label1.setAutoFillBackground(True) 
        palette = QPalette()   
        palette.setColor(QPalette.Window,Qt.blue)  
        label1.setPalette(palette) 
        label1.setAlignment( Qt.AlignCenter)
          
        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")
        
        label3.setAlignment( Qt.AlignCenter)    
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap( QPixmap("./images/python.jpg"))

        label4.setText("<A href='http://www.cnblogs.com/wangshuo1/'>欢迎访问信平的小屋</a>")
        label4.setAlignment( Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')
        
        #2
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget( label3 )
        vbox.addStretch()
        vbox.addWidget( label4)
        
        #3
        label1.setOpenExternalLinks(True)
        # 打开允许访问超链接,默认是不允许，需要使用 setOpenExternalLinks(True)允许浏览器访问超链接
        label4.setOpenExternalLinks( False )
        # 点击文本框绑定槽事件  
        label4.linkActivated.connect( link_clicked )
        
        # 划过文本框绑定槽事件       
        label2.linkHovered.connect( link_hovered )
        label1.setTextInteractionFlags( Qt.TextSelectableByMouse )

        self.setLayout(vbox)
        self.setWindowTitle("QLabel 例子")
        
def link_hovered():
    print("当鼠标滑过label-2标签时，触发事件。")
        
def link_clicked():
    print("当鼠标点击label-4标签时，触发事件。" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())
