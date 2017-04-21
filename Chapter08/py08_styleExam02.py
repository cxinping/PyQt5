# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QPalette , QBrush , QPixmap

class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.setWindowTitle("界面背景图片设置") 
		self.resize(350,  250)  
		palette	= QPalette()
		palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/python.jpg")))
		self.setPalette(palette)  
        
if __name__ == "__main__": 
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())
