# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子
   
  
'''

import sys
from PyQt5.QtWidgets import *

from DataGrid import DataGrid


if __name__ == '__main__':
	app =  QApplication(sys.argv)
	demo = DataGrid()
	demo.show()
	sys.exit(app.exec_())
		
