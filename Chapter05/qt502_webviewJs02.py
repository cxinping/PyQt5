# -*- coding: utf-8 -*- 

'''
    【简介】
	QWebView中网页调用JavaScript 
  
'''


from PyQt5 import QtWidgets 
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWebChannel import  QWebChannel 

from PyQt5.QtCore import QUrl  
from MySharedObject  import MySharedObject
import sys


# Create an application
app = QtWidgets.QApplication(sys.argv)

# And a window5
win = QtWidgets.QWidget()
win.setWindowTitle('QWebView Interactive Demo')

# And give it a layout
layout = QtWidgets.QVBoxLayout()
win.setLayout(layout)

# Create and fill a QWebView
#view = QtWebKitWidgets.QWebView()  # depecated?
view = QtWebEngineWidgets.QWebEngineView()
htmlUrl = 'http://127.0.0.1:8020/TestWeb/index.html'
view.load( QUrl( htmlUrl ))

# A button to call our JavaScript
button = QtWidgets.QPushButton('Set Full Name')

channel =  QWebChannel( )
myObj = MySharedObject()
#print( myObj.name2)

channel.registerObject( "bridge", myObj )


view.page().setWebChannel(channel)
button2 = QtWidgets.QPushButton('get value')
 

def js_callback(result):
	print(result)
    
def complete_name():
	view.page().runJavaScript('completeAndReturnName();', js_callback)

def sayHello():
	print('hello')
    
    
# Connect 'complete_name' to the button's 'clicked' signal
button.clicked.connect(complete_name)
button2.clicked.connect(sayHello)

# Add the QWebView and button to the layout
layout.addWidget(view)
layout.addWidget(button)
layout.addWidget(button2)

# Show the window and run the app
win.show()

sys.exit(app.exec_())
