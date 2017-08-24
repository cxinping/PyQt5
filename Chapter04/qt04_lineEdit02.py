# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QLineEdit的验证器例子     
  
'''

from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,  QFormLayout
from PyQt5.QtGui import QIntValidator ,QDoubleValidator  , QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys  

class lineEditDemo(QWidget):
	def __init__(self, parent=None):
		super(lineEditDemo, self).__init__(parent)
		self.setWindowTitle("QLineEdit例子")

		flo = QFormLayout()
		pIntLineEdit  = QLineEdit( )
		pDoubleLineEdit  = QLineEdit()
		pValidatorLineEdit  = QLineEdit( )

		flo.addRow("整形", pIntLineEdit)
		flo.addRow("浮点型", pDoubleLineEdit)
		flo.addRow("字母和数字", pValidatorLineEdit)
        
		pIntLineEdit.setPlaceholderText("整形");
		pDoubleLineEdit.setPlaceholderText("浮点型");
		pValidatorLineEdit.setPlaceholderText("字母和数字");

		# 整形 范围：[1, 99]
		pIntValidator = QIntValidator(self)
		pIntValidator.setRange(1, 99)

		# 浮点型 范围：[-360, 360] 精度：小数点后2位
		pDoubleValidator = QDoubleValidator(self)
		pDoubleValidator.setRange(-360, 360)
		pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
		pDoubleValidator.setDecimals(2)
		
		# 字符和数字
		reg = QRegExp("[a-zA-Z0-9]+$")
		pValidator = QRegExpValidator(self)
		pValidator.setRegExp(reg)	

        # 设置验证器
		pIntLineEdit.setValidator(pIntValidator)
		pDoubleLineEdit.setValidator(pDoubleValidator)
		pValidatorLineEdit.setValidator(pValidator)
		                    
		self.setLayout(flo)                        
   
if __name__ == "__main__":       
	app = QApplication(sys.argv)
	win = lineEditDemo()	
	win.show()	
	sys.exit(app.exec_())
