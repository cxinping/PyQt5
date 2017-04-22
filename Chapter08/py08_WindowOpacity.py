# -*- coding: utf-8 -*-

'''
    【简介】
	设置窗口的透明度
    
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("窗口的透明度设置") 
    win.setWindowOpacity(0.5)
    
    win.resize(350,  250) 
    win.show()
    sys.exit(app.exec_())

