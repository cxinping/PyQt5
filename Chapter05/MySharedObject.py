# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty

class MySharedObject(QObject):
	name2 = 'aaa'
        
	def __init__( self):
		super( MySharedObject, self).__init__()
		self.name = 'wangwu'
		#self.intValue = 100
            
	def sayHello( self):
        # 发射信号
		print('Hi Pyqt5')

	def _getIntValue( self):
        # 发射信号
		return '111'        
	
	intValue = pyqtProperty(str, fget=_getIntValue)          
        
