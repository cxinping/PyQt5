# -*- coding: utf-8 -*-
 
class MyClass(object):
	def __init__(self):
		self._param = None  

	@property  
	def param(self):  
		print( "get param: %s" % self._param)
		return self._param  

	@param.setter  
	def param(self, value):  
		print( "set param: %s" % self._param )
		self._param = value  
	 
	@param.deleter  
	def param(self):  
		print( "del param: %s" % self._param)
		del self._param  

if __name__ == "__main__":
	cls = MyClass()
	cls.param = 10
	print("current param : %s " % cls.param )
	del cls.param
    