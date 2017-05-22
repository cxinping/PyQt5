# -*- coding: utf-8 -*-

"""
    【简介】
    国际化例子


"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QVBoxLayout , QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle(self.tr('title')) 
		self.resize(330, 130)  
		vlayout = QVBoxLayout()
		vlayout.addWidget( QPushButton( self.tr('upload')) )
		vlayout.addWidget( QPushButton( self.tr('download')) )
		self.setLayout(vlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
		
