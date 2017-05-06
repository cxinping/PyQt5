# -*- coding: utf-8 -*- 

'''
    【简介】
	QWebView打开网页例子 
  
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):

	def __init__(self ):
		super(QMainWindow, self).__init__()
		self.setWindowTitle('QWebView打开网页例子')
		self.setGeometry(5, 30, 1355, 730)
		self.browser = QWebEngineView()
        #1 加载外部页面
        #self.browser.load(QUrl('https://www.sogou.com/'))
		
        #2 加载本地页面
		url = r'E:\quant\PyQt5\Chapter05\index.html'
		self.browser.load( QUrl( url ));
		
		self.setCentralWidget(self.browser)

if __name__ == '__main__':
	app = QApplication(sys.argv)
    
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())
