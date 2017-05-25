# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import *
from MatrixWinUi import *

class CallMatrixWinUi(QWidget ):
	def __init__(self, parent=None):    
		super(CallMatrixWinUi, self).__init__(parent)
		self.ui = Ui_MatrixWin()
		self.ui.setupUi(self)

	# 获得一量杯的酒
	def getJiggers(self):
	   # Return the total volume of the margaritas in units of jiggers.
	   # One jigger is 0.0444 liters.
	
		jiggersTequila = self.ui.tequilaScrollBar.value()
		jiggersTripleSec = self.ui.tripleSecSpinBox.value()
		jiggersLimeJuice = float(self.ui.limeJuiceLineEdit.text())
		jiggersIce = self.ui.iceHorizontalSlider.value()
		return jiggersTequila + jiggersTripleSec + jiggersLimeJuice + jiggersIce

	# 获得升
	def getLiters(self):
		'''Return the total volume of the margaritas in liters.'''
		return 0.0444 * self.getJiggers()

	# 获得搅拌速度
	def getSpeedName(self):
		speedButton = self.ui.speedButtonGroup.checkedButton()
		if speedButton is None:
			return None
		return speedButton.text()

	def uiAccept(self):
		print('* CallMatrixWinUi accept ')
		'''Execute the command in response to the OK button.'''
		print('The volume of drinks is {0} liters ({1} jiggers).'.format(self.getLiters() , self.getJiggers() ))
		print('The blender is running at speed "{0}"'.format(self.getSpeedName() ))
		#self.close()

	# 点击cancel按钮，关闭窗口	
	def uiReject(self):
		print('* CallMatrixWinUi reject ')
		'''Cancel.'''
		self.close()
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	demo = CallMatrixWinUi()  
	demo.show()  
	sys.exit(app.exec_())  
