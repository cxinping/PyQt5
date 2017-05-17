#!/usr/bin/env python3

'''
    【简介】
	PyQT5中 QTreeView 例子
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl  
from PyQt5.QtNetwork import QNetworkAccessManager , QNetworkRequest ,QNetworkReply  

class MainWidget(QWidget):

	def __init__(self, parent=None):
		super(MainWidget, self).__init__(parent=parent)    
		
		manager = QNetworkAccessManager( self )
		manager.finished.connect( self.onFinished)
		
		#url = QUrl("http://www.163.com/")
		url = QUrl("http://www.baiduaaaaaaabbbbbb.com/")
		request = QNetworkRequest( url ) 
		manager.get( request )
		
		

	def onFinished(self, reply ):
		print('--- onFinished ----')
		
		if reply.error() == QNetworkReply.NoError : 
			print( reply.readAll() )
			 						
		else  : 	
			print('---error 2')
			reason = reply.attribute( QNetworkRequest.HttpReasonPhraseAttribute ) 
			status = reply.attribute( QNetworkRequest.HttpStatusCodeAttribute ) 
			failedUrl =	reply.request().url()
			
			print('reply.error=%s, error message=%s' % (reply.error() , reply.errorString()  ) )		
			print('reason=%s, status=%s' % ( reason , status ) )					
			
			print( failedUrl )
 
		
if __name__ == "__main__":
	app =  QApplication([])
	main = MainWidget()
	main.show()
	sys.exit(app.exec_())  
