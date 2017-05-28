# -*- coding: utf-8 -*-

"""
    【简介】
    自动化测试用例


"""

import sys
import unittest
import HTMLTestRunner
import time
from PyQt5.QtWidgets import *
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt , QThread  ,  pyqtSignal
import CallMatrixWinUi

# 继承 QThread 类
class BackWorkThread(QThread):  
	# 声明一个信号，同时返回一个str
	finishSignal = pyqtSignal(str)
	# 构造函数里增加形参
	def __init__(self, sleepTime,parent=None):
		super(BackWorkThread, self).__init__(parent)
		# 储存参数
		self.sleepTime = sleepTime

	#重写run()函数，在里面定时执行业务。
	def run(self):
		# 休眠一段时间
		time.sleep(self.sleepTime)
		# 休眠结束，发送一个信号告诉主线程窗口
		self.finishSignal.emit('ok , begin to close Window')
		
class MatrixWinTest(unittest.TestCase):  
    # 初始化工作  
	def setUp(self):  
		print('*** setUp ***')
		self.app = QApplication(sys.argv)	
		self.form = CallMatrixWinUi.CallMatrixWinUi()
		self.form.show()		
		
		# 新建对象，传入参数。每5秒执行一个测试用例 TestCase。
		self.bkThread = BackWorkThread(int( 5 ))
		# 连接子进程的信号和槽函数
		self.bkThread.finishSignal.connect(self.closeWindow)
		#self.bkThread.finishSignal.connect(self.app.exec_)
		
		# 启动线程，开始执行run()函数里的内容
		self.bkThread.start()
		        
	# 退出清理工作  
	def tearDown(self):  
		print('*** tearDown ***')
		self.app.exec_()  		
	
	# 设置窗口中所有部件的值为0，状态为初始状态。	
	def setFormToZero(self):
		print('* setFormToZero *')  				
		self.form.ui.tequilaScrollBar.setValue(0)
		self.form.ui.tripleSecSpinBox.setValue(0)
		self.form.ui.limeJuiceLineEdit.setText("0.0")
		self.form.ui.iceHorizontalSlider.setValue(0)
		
		self.form.ui.selScrollBarLbl.setText("0")	
		self.form.ui.selIceSliderLbl.setText("0")	
		
	# 关闭窗口
	def closeWindow(self):
		print( '*  关闭窗口')
		self.app.quit()
		
	# 测试用例-在默认状态下的测试GUI	
	def test_defaults(self):
		'''测试GUI处于默认状态'''
		print('*** testCase test_defaults begin ***')
		self.form.setWindowTitle('开始测试用例 test_defaults ')
				
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
		self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
		self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
		self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop") 		
		print('*** speedName='+ self.form.getSpeedName() )
	
		# 用鼠标左键按OK		
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		
		# 即使没有按OK，Class也处于默认状态
		self.assertEqual(self.form.getJiggers() , 36.0)
		self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
		print('*** testCase test_defaults end ***')		      	
		
	# 测试用例-测试滚动条
	def test_moveScrollBar(self):
		'''测试用例test_moveScrollBar'''	
		print('*** testCase test_moveScrollBar begin ***')
		self.form.setWindowTitle('开始测试用例 test_moveScrollBar ')	
		self.setFormToZero()
		
        # 测试将龙舌兰酒的滚动条的值设定为 12 ，ui中它实际的最大值为 11
		self.form.ui.tequilaScrollBar.setValue( 12 )
		print('* 当执行self.form.ui.tequilaScrollBar.setValue(12) 后，ui.tequilaScrollBar.value() => ' + str( self.form.ui.tequilaScrollBar.value() ) )
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11 )
		
        # 测试将龙舌兰酒的滚动条的值设定为 -1 ，ui中它实际的最小值为 0
		self.form.ui.tequilaScrollBar.setValue(-1)
		print('* 当执行self.form.ui.tequilaScrollBar.setValue(-1) 后，ui.tequilaScrollBar.value() => ' + str( self.form.ui.tequilaScrollBar.value() ) )
		self.assertEqual(self.form.ui.tequilaScrollBar.value(), 0)
		
		# 重新将将龙舌兰酒的滚动条的值设定为 5
		self.form.ui.tequilaScrollBar.setValue(5)
				
        # 用鼠标左键按OK按钮
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers() , 5)
		print('*** testCase test_moveScrollBar end ***')

	# 测试用例-测试滚动条
	def test_tripleSecSpinBox(self):
		'''测试用例 test_tripleSecSpinBox '''	
		print('*** testCase test_tripleSecSpinBox begin ***')
		self.form.setWindowTitle('开始测试用例 test_tripleSecSpinBox ')	
		'''测试修改spinBox部件的最大最小值
			测试它的最小和最大值作为读者的练习。
        '''		
		self.setFormToZero()
		# tripleSecSpinBox在界面中的取值范围为 0 到 11， 将它的最大值设为 12，看是否显示正常。
		self.form.ui.tripleSecSpinBox.setValue(12)
		print('* 当执行self.form.ui.tripleSecSpinBox.setValue(12) 后，ui.tripleSecSpinBox.value() => ' + str( self.form.ui.tripleSecSpinBox.value() ) )				
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 11 )	

		# tripleSecSpinBox在界面中的取值范围为 0 到 11， 将它的最小值设为 -1， 看是否显示正常。
		self.form.ui.tripleSecSpinBox.setValue(-1)
		print('* 当执行self.form.ui.tripleSecSpinBox.setValue(-1) 后，ui.tripleSecSpinBox.value() => ' + str( self.form.ui.tripleSecSpinBox.value() ) )				
		self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 0 )	
		
		self.form.ui.tripleSecSpinBox.setValue(2)

        # 用鼠标左键按OK按钮
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers(), 2)		
		print('*** testCase test_tripleSecSpinBox end ***')

	# 测试用例-测试柠檬汁单行文本框		
	def test_limeJuiceLineEdit(self):
		'''测试用例 test_limeJuiceLineEdit '''	
		print('*** testCase test_limeJuiceLineEdit begin ***')
		self.form.setWindowTitle('开始测试用例 test_limeJuiceLineEdit ')			
		'''测试修改juice line edit部件的最大最小值
		测试它的最小和最大值作为读者的练习。
		'''
		self.setFormToZero()		
        # 清除lineEdit小部件值，然后在lineEdit小部件中键入“3.5”
		self.form.ui.limeJuiceLineEdit.clear()		
		QTest.keyClicks(self.form.ui.limeJuiceLineEdit, "3.5")
		
        # 用鼠标左键按OK按钮
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers() , 3.5)
		print('*** testCase test_limeJuiceLineEdit end ***')

	# 测试用例-测试iceHorizontalSlider
	def test_iceHorizontalSlider(self):
		'''测试用例 test_iceHorizontalSlider '''	
		print('*** testCase test_iceHorizontalSlider begin ***')	
		self.form.setWindowTitle('开始测试用例 test_iceHorizontalSlider ')	
				
		'''测试ice slider.
		测试它的最小和最大值作为读者的练习。
		'''
		self.setFormToZero()
		self.form.ui.iceHorizontalSlider.setValue(4)

		# 用鼠标左键按OK按钮
		okWidget = self.form.ui.okBtn
		QTest.mouseClick(okWidget, Qt.LeftButton)
		self.assertEqual(self.form.getJiggers(), 4)		
		print('*** testCase test_iceHorizontalSlider end ***')

	# 测试用例- 
	def test_liters(self):
		'''测试用例 test_liters '''		
		print('*** testCase test_liters begin ***')		
		self.form.setWindowTitle('开始测试用例 test_liters ')	
		
		self.setFormToZero()
		self.assertAlmostEqual(self.form.getLiters() , 0.0)
		self.form.ui.iceHorizontalSlider.setValue(1 )
		self.assertAlmostEqual(self.form.getLiters(), 0.0444)
		self.form.ui.iceHorizontalSlider.setValue(2)
		self.assertAlmostEqual(self.form.getLiters(), 0.0444 * 2)
		print('*** testCase test_liters end ***')

	# 测试用例- 		
	def test_blenderSpeedButtons(self):
		print('*** testCase test_blenderSpeedButtons begin ***')		
		'''测试选择搅拌速度按钮'''
		self.form.ui.speedButton1.click()
		self.assertEqual(self.form.getSpeedName(), "&Mix")		
		self.form.ui.speedButton2.click()
		self.assertEqual(self.form.getSpeedName(), "&Whip")
		self.form.ui.speedButton3.click()
		self.assertEqual(self.form.getSpeedName(), "&Puree")		
		self.form.ui.speedButton4.click()
		self.assertEqual(self.form.getSpeedName(), "&Chop")
		self.form.ui.speedButton5.click()
		self.assertEqual(self.form.getSpeedName(), "&Karate Chop")		
		self.form.ui.speedButton6.click()
		self.assertEqual(self.form.getSpeedName(), "&Beat")
		self.form.ui.speedButton7.click()
		self.assertEqual(self.form.getSpeedName(), "&Smash")
		self.form.ui.speedButton8.click()
		self.assertEqual(self.form.getSpeedName(), "&Liquefy")
		self.form.ui.speedButton9.click()
		self.assertEqual(self.form.getSpeedName(), "&Vaporize")		
		print('*** testCase test_blenderSpeedButtons end ***')

def runUnitTest1(  ):
	# 默认测试所有的测试用例
	unittest.main() 	

def runUnitTest2(  ):
	# 按照指定顺序执行测试用例
	suite = unittest.TestSuite()
	suite.addTest(MatrixWinTest("test_defaults"))
	#suite.addTest(MatrixWinTest("test_moveScrollBar"))
	#suite.addTest(MatrixWinTest("test_tripleSecSpinBox"))
	#suite.addTest(MatrixWinTest("test_limeJuiceLineEdit"))
	#suite.addTest(MatrixWinTest("test_iceHorizontalSlider"))
	#suite.addTest(MatrixWinTest("test_liters"))
	#suite.addTest(MatrixWinTest("test_blenderSpeedButtons"))    	
	runner = unittest.TextTestRunner()
	runner.run(suite)
	
if __name__ == "__main__":  
	#runUnitTest1()
    runUnitTest2()
	

	
	
	
	
	
