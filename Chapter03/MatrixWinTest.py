# -*- coding: utf-8 -*-

"""
    【简介】
    测试用例


"""

import sys
import unittest
from PyQt5.QtWidgets import QApplication  ,QWidget ,QVBoxLayout , QPushButton
from PyQt5.QtGui import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import CallMatrixWinUi

class Winform(unittest.TestCase):

    # 初始化工作  
	def setUp(self):  
		print('--- setUp ---')
		self.form = CallMatrixWinUi.CallMatrixWinUi()
		self.form.show()		
		print( self.form )
	  
	# 退出清理工作  
	def tearDown(self):  
		print('--- tearDown ---')  
		
	def setFormToZero(self):
		print('* setFormToZero ---')  
		self.form.ui.tequilaScrollBar.setValue(0)
  
	# 测试滚动条
	def test_moveScrollBar(self):		
		print('* test_tequilaScrollBar ---')
		#self.setFormToZero()
  
if __name__ == "__main__":  
	app = QApplication(sys.argv)	
	unittest.main() 	
	sys.exit(app.exec_())
