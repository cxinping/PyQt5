# -*- coding: utf-8 -*- 
'''
    【简介】
	QWebView打开网页
  
  
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):

    def __init__(self ):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('简单浏览器')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.sogou.com/'))

        self.setCentralWidget(self.browser)

if __name__ == '__main__':
      app = QApplication(sys.argv)
      win = MainWindow()
      win.show()
      app.exec_()