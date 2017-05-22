# -*- coding: utf-8 -*-
 
class MyClass(object):
    def __init__(self):
        self._param = None

    def getParam(self):
        print( "get param: %s" % self._param)
        return self._param

    def setParam(self, value):
        print( "set param: %s" % self._param )
        self._param = value

    def delParam(self):
        print( "del param: %s" % self._param)
        del self._param

    param = property(getParam, setParam, delParam)

if __name__ == "__main__":
    cls = MyClass()
    cls.param = 10
    print("current param : %s " % cls.param )
    del cls.param