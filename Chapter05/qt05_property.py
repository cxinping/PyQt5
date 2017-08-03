# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, pyqtProperty

class MyObject(QObject):
	def __init__(self, inVal=20):
		self.val = inVal

	def readVal(self):
		print('readVal=%s' %  self.val )  
		return self.val

	def setVal(self,val):
		print('setVal=%s' %  val )    
		self.val = val

	ppVal = pyqtProperty(int, readVal, setVal )
			
if __name__ == '__main__':
	obj = MyObject()
	print('\n#1')		
	obj.ppVal = 10
	print('\n#2')	
	print( 'obj.ppVal=%s' % obj.ppVal ) 
	print( 'obj.readVal()=%s' % obj.readVal() ) 
	
