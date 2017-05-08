# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QCheckBox 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class CheckBoxDemo(QWidget):

	def __init__(self, parent=None):
		super(CheckBoxDemo , self).__init__(parent)
		
		groupBox = QGroupBox("Checkboxes")
		groupBox.setFlat( False )
		
		layout = QHBoxLayout()
		self.checkBox1= QCheckBox("&Checkbox1")
		self.checkBox1.setChecked(True)
		self.checkBox1.stateChanged.connect( lambda:self.btnstate(self.checkBox1) )
		layout.addWidget(self.checkBox1)
        
		self.checkBox2 = QCheckBox("Checkbox2")
		self.checkBox2.toggled.connect( lambda:self.btnstate(self.checkBox2) )
		layout.addWidget(self.checkBox2)

		self.checkBox3 = QCheckBox("tristateBox")
		self.checkBox3.setTristate(True)
		self.checkBox3.setCheckState(Qt.PartiallyChecked )		
		self.checkBox3.stateChanged.connect( lambda:self.btnstate(self.checkBox3) )
		layout.addWidget(self.checkBox3)
        
		groupBox.setLayout(layout)
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(groupBox)
		
		self.setLayout(mainLayout)
		self.setWindowTitle("checkbox demo")
	
	def btnstate(self,btn ):
		chk1Status = self.checkBox1.text()+", isChecked="+  str( self.checkBox1.isChecked() ) + ', chekState=' + str(self.checkBox1.checkState())   +"\n"		 
		chk2Status = self.checkBox2.text()+", isChecked="+  str( self.checkBox2.isChecked() ) + ', checkState=' + str(self.checkBox2.checkState())   +"\n"	
		chk3Status = self.checkBox3.text()+", isChecked="+  str( self.checkBox3.isChecked() ) + ', checkState=' + str(self.checkBox3.checkState())   +"\n"			
		print(chk1Status + chk2Status + chk3Status )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	checkboxDemo = CheckBoxDemo()
	checkboxDemo.show()
	sys.exit(app.exec_())
