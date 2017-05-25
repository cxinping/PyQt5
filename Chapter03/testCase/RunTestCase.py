# -*- coding: utf-8 -*-

"""
    【简介】
    自动画测试用例


"""

import sys
import unittest
import HTMLTestRunner
import time
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt , QThread  ,  pyqtSignal

from MatrixWinTest import MatrixWinTest
	
if __name__ == "__main__":  
	#runUnitTest1()
    #runUnitTest2()
	#runUnitTest3()
	
	now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))	
	print( now )
	testunit = unittest.TestSuite()
	testunit.addTest(unittest.makeSuite(MatrixWinTest ))
	
	#testunit.addTest(MatrixWinTest("test_defaults"))
	#testunit.addTest(MatrixWinTest("test_moveScrollBar"))
	#testunit.addTest(MatrixWinTest("test_tripleSecSpinBox"))
	#testunit.addTest(MatrixWinTest("test_limeJuiceLineEdit"))
	#testunit.addTest(MatrixWinTest("test_iceHorizontalSlider"))
	#testunit.addTest(MatrixWinTest("test_liters"))
	#testunit.addTest(MatrixWinTest("test_blenderSpeedButtons"))  
    
	htmlFile = ".\\"+now+"HTMLtemplate.html"
	print( 'htmlFile='+ htmlFile)
	fp = open(htmlFile,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp, 
		title=u"PyQt5测试报告", 
		description=u"用例测试情况")
	runner.run(testunit)
	fp.close()
	
	
	
	
	
