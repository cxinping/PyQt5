# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from Plotly_PyQt5 import Plotly_PyQt5


class MainWindow(QMainWindow ):

	def __init__(self ):
		super(QMainWindow, self).__init__()
		self.plotly_pyqt5 = Plotly_PyQt5()
		self.qwebengine = QWebEngineView()   		
		self.qwebengine.setGeometry(QRect(50, 20, 1200, 600))
		print( self.plotly_pyqt5.get_plotly_path_if_hs300_bais() )
		self.qwebengine.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.showMaximized()
	app.exec_()
