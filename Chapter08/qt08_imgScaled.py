# -*- coding: utf-8 -*-

'''
    【简介】
	图片大小缩放
    
'''

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5.QtGui   import QImage , QPixmap 
from PyQt5.QtCore import Qt 
import sys

class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
        filename = r".\images\Cloudy_72px.png"
        img = QImage( filename )
               
        label1 = QLabel(self)
        label1.setFixedWidth(120)
        label1.setFixedHeight(120)
         
        result = img.scaled(label1.width(), label1.height(),Qt.IgnoreAspectRatio, Qt.SmoothTransformation);
        label1.setPixmap(QPixmap.fromImage(result))
        
        #3
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
      
        self.setLayout(vbox)
        self.setWindowTitle("图片大小缩放例子")
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())

