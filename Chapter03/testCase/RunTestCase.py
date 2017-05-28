# -*- coding: utf-8 -*-

"""
    【简介】
    自动化测试用例


"""
 
import unittest
import HTMLTestRunner
import time   
from MatrixWinTest import MatrixWinTest
	
if __name__ == "__main__":  
    
	now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))	
	print( now )
	testunit = unittest.TestSuite()
	testunit.addTest(unittest.makeSuite(MatrixWinTest ))
	    
	htmlFile = ".\\"+now+"HTMLtemplate.html"
	print( 'htmlFile='+ htmlFile)
	fp = open(htmlFile,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp, 
		title=u"PyQt5测试报告", 
		description=u"用例测试情况")
	runner.run(testunit)
	fp.close()
	
	
	
	
	
