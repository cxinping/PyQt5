# -*- coding: utf-8 -*-

'''
    【简介】
	 界面背景图片设置
    
'''

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QPalette , QBrush , QPixmap


app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("界面背景图片设置") 
palette	= QPalette()
palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/python.jpg")))
win.setPalette(palette)  
#当背景图片的宽度和高度大于窗口的宽度和高度时
#win.resize(460,  255 )  

#当背景图片的宽度和高度小于窗口的宽度和高度时
win.resize(800,  600 )  
win.show()
sys.exit(app.exec_())
