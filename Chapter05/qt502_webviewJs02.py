# -*- coding: utf-8 -*- 

'''
    【简介】
	QWebView中网页调用JavaScript 
  
'''

from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  
from MySharedObject  import MySharedObject
from PyQt5.QtWebChannel import  QWebChannel 
import sys


# 创建一个 application实例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web页面中的JavaScript与 QWebEngineView交互例子')

# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个 QWebEngineView 对象
view =  QWebEngineView()
htmlUrl = 'http://127.0.0.1:8020/web/index.html'
view.load( QUrl( htmlUrl ))

# 创建一个 QWebChannel对象，用来传递pyqt参数到JavaScript
channel =  QWebChannel( )
myObj = MySharedObject()   
channel.registerObject( "bridge", myObj )  
view.page().setWebChannel(channel)
 
# 把QWebView和button加载到layout布局中
layout.addWidget(view)
           
# 显示窗口和运行app
win.show()
sys.exit(app.exec_())
