# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import *
from MatrixWinUi import *

class MainWindowTest(QWidget ):
	def __init__(self, parent=None):    
		super(MainWindowTest, self).__init__(parent)
		self.ui = Ui_MatrixWin()
		self.ui.setupUi(self)
            
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	demo = MainWindowTest()  
	demo.show()  
	sys.exit(app.exec_())  
