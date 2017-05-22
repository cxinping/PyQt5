# -*- coding: utf-8 -*-

"""
    【简介】
    测试用例


"""

import sys
import unittest
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import CallMatrixWinUi

class MatrixWinTest(unittest.TestCase):

    # 初始化工作  
	def setUp(self):  
		print('--- setUp ---')
		self.app = QApplication(sys.argv)	
		self.form = CallMatrixWinUi.CallMatrixWinUi()
		self.form.show()
		        	  
	# 退出清理工作  
	def tearDown(self):  
		print('--- tearDown ---')  
		#self.app.deleteLater()
		sys.exit(self.app.exec_())
		
	def setFormToZero(self):
		print('* setFormToZero ---')  
		self.form.ui.tequilaScrollBar.setValue(0)

		# Test the maximum.  This one goes to 11.
		self.form.ui.tequilaScrollBar.setValue(12)
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11)

	def test_defaults(self):
		'''Test the GUI in its default state'''
		print('* test_defaults ---')
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8 )
		            		
		# Push OK with the left mouse button
		okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
		QTest.mouseClick(okWidget, Qt.LeftButton)
		
		
	# 测试滚动条
	def test_moveScrollBar(self):		
		print('* test_moveScrollBar ---')
		self.setFormToZero()
		    			
        # Push OK with the left mouse button
		okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
		QTest.mouseClick(okWidget, Qt.LeftButton)

	
if __name__ == "__main__":  
	#app = QApplication(sys.argv)	
	unittest.main() 	
	
	#suite = unittest.TestSuite()
	#suite.addTest(MatrixWinTest("test_defaults"))
	#runner = unittest.TextTestRunner()
	#runner.run(suite)
	
	#sys.exit(app.exec_())
