# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtProperty

class MyObject(QObject):
	def __init__(self, inVal=42):
		self.val = inVal

	def readVal(self):
		print('read val: %s' %  self.val )  
		return self.val

	def setVal(self,val):
		print('set val: %s' %  val )    
		self.val = val

	pp = pyqtProperty(int, readVal, setVal )
		
if __name__ == '__main__':
	obj = MyObject()
	obj.pp = 10
	print( 'get val: %s' % obj.pp) 
