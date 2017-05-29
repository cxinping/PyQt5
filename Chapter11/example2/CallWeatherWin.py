# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow ):
	def __init__(self, parent=None):    
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
 		
	def queryWeather(self):
		rep = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
		rep.encoding = 'utf-8'

		print( rep.json() ) 
		print('城市: %s' % rep.json()['weatherinfo']['city'] )
		print('风向: %s' % rep.json()['weatherinfo']['WD'] )
		print('温度: %s' % rep.json()['weatherinfo']['temp'] + " 度")
		print('风力: %s' % rep.json()['weatherinfo']['WS'] )
		print('湿度: %s' % rep.json()['weatherinfo']['SD'] )
	
		print('* queryWeather reject ')

	def clearResult(self):
		print('* clearResult reject ')
		self.ui.resultText.clear()	
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainWindow()  
	win.show()  
	sys.exit(app.exec_())  
