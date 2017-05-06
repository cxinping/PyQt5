# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget,QMessageBox

class MySharedObject(QWidget):
        
	def __init__( self):
		super( MySharedObject, self).__init__()
		            
	def _getStrValue( self):
        #  
		return '100'        

	def _setStrValue( self,  str ):
        #  
		print('获得页面参数 ：%s'% str ) 
		QMessageBox.information(self,"Information", '获得页面参数 ：%s'% str )
        
    #需要定义对外发布的方法    
	strValue = pyqtProperty(str, fget=_getStrValue, fset=_setStrValue)     
    
    
    
    
    
