#!/usr/bin/env python3

'''
    【简介】
	PyQT5中 QTreeView 例子
   
  
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl , QDir  ,QFile, QIODevice 
from PyQt5.QtNetwork import QNetworkAccessManager , QNetworkRequest ,QNetworkReply  

class MainWidget(QWidget):

	def __init__(self, parent=None):
		super(MainWidget, self).__init__(parent=parent)    
		
		manager = QNetworkAccessManager( self )
		manager.finished.connect( self.onFinished)
		
		url = QUrl("http://www.cnblogs.com/li-peng/p/3656613.html")
		#url = QUrl("http://www.baiduaaaaaaabbbbbb.com/")
		request = QNetworkRequest( url ) 
		manager.get( request )
		
		

	def onFinished(self, reply ):
		print('--- onFinished ----')
		
		if reply.error() == QNetworkReply.NoError : 		
			thefileName  = 'index.html'
			thePath = r"E:/mydownload/"
			createfile = QDir() 
			exist = createfile.exists(thePath)
			if not exist : 
				createfile.mkpath(thePath)
			
			thePath += thefileName;
			file =  QFile(thePath);
			print( thePath )
			if file.open(QIODevice.Append) :
				file.write(reply.readAll())
				file.flush()
				file.close()
			#print( reply.readAll() )
			 						
		else  : 	
			print('---error 2')
			reason = reply.attribute( QNetworkRequest.HttpReasonPhraseAttribute ) 
			status = reply.attribute( QNetworkRequest.HttpStatusCodeAttribute ) 
			failedUrl =	reply.request().url()
			
			print('reply.error=%s, error message=%s' % (reply.error() , reply.errorString()  ) )		
			print('reason=%s, status=%s' % ( reason , status ) )					
			
			print( failedUrl )
 
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	main = MainWidget()
	main.show()
	sys.exit(app.exec_())  
