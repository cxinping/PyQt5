# -*- coding: utf-8 -*- 

'''
    【简介】
	QWebEngineView加载网页，使网页中的用JavaScript 失效
  
'''

from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView , QWebEngineSettings 
from PyQt5.QtCore import QUrl  
from MySharedObject  import MySharedObject
from PyQt5.QtWebChannel import  QWebChannel 
from PyQt5.QtGui import QIcon
import sys

class Web(QWebEngineView):

	def load(self, url):
		self.setUrl(QUrl(url))

	def adjustTitle(self):
		#self.setWindowTitle(self.title())
		pass

	def disableJS(self):
		settings = QWebEngineSettings.globalSettings()
		settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)
		
class Main(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Name')
		self.setWindowIcon(QIcon('./images/cartoon1.ico'))  
		web = Web()                                         
		
		web.load("http://127.0.0.1:8020/web/index2.html")
		web.disableJS()
		
		self.btn = QPushButton('Button', self)
		self.btn.resize(self.btn.sizeHint())
		lay = QVBoxLayout(self)
		lay.addWidget(self.btn)
		lay.addWidget(web)
		
if __name__=="__main__":  
	app = QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())


