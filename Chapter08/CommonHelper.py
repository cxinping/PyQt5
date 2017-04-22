# -*- coding: utf-8 -*-

from PyQt5.QtCore import QFile

class CommonHelper :
    def __init__(self ) :
        pass
    
    @staticmethod
    def setStyle11(  style) :
       
        qss = QFile(style)
        qss.open( QFile.ReadOnly )
        print( type( qss.readAll() ) )
        return qss.readAll()
     
    @staticmethod    
    def readQss( style):
        with open( style , 'r') as f:
           return f.read()
    
    
if __name__ == "__main__": 
    styleFile = r'e:\main.qss'
    #CommonHelper.setStyle( styleFile )
    CommonHelper.readQss( styleFile )
