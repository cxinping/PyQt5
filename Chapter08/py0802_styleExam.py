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
win.resize(350,  250)  
palette	= QPalette()
palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/python.jpg")))
win.setPalette(palette)  
win.show()
sys.exit(app.exec_())
