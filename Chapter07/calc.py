# -*- coding: utf-8 -*-

"""
    【简介】信号/槽的装饰器实现方式
   


"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from ui_calc import Ui_Calc
 
class MyCalc(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_Calc()
		self.ui.setupUi(self)

	@pyqtSlot(int)
	def on_inputSpinBox1_valueChanged(self, value):
		self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))

	@pyqtSlot(int)
	def on_inputSpinBox2_valueChanged(self, value):
		self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MyCalc()
	win.show()
	sys.exit(app.exec_())