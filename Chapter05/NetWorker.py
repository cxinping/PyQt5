# -*- coding: utf-8 -*- 

'''
    【简介】
	NewWorker 网络工具类   
  
'''
from PyQt5.QtCore import QUrl , QDir  ,QFile, QIODevice 
from PyQt5.QtNetwork import QNetworkAccessManager , QNetworkRequest ,QNetworkReply  
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
import sys

class NewWorker:
	def __init__(self ):
		print('----- __init__ ---')
		self.manager = QNetworkAccessManager()
		self.manager.finished.connect( self.onFinished)
		
	def get(self, url ):
		print('----- get %s' % url )
		request = QNetworkRequest( QUrl(url) ) 
		return self.manager.get( request )
		
	def onFinished(self, reply ):	
		print('--- onFinieshed ---');
		print( reply.readAll() )
	 
		
if __name__ == '__main__':
	app =  QApplication([])
	network =  NewWorker()
	reply = network.get('http://www.baidu.com')
	#print( reply.readAll() )
	sys.exit(app.exec_()) 
