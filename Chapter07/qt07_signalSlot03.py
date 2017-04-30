# -*- coding: utf-8 -*-

"""
    【简介】
    信号槽N对N连接、断开连接示例


"""

from PyQt5.QtCore import QObject , pyqtSignal

class SignalClass(QObject):

    # 声明一个无参数的信号
	signal1 = pyqtSignal()

    # 声明带一个int类型参数的信号
	signal2 = pyqtSignal(int)

	def __init__(self,parent=None):
		super(SignalClass,self).__init__(parent)

		# 信号sin1连接到sin1Call和sin2Call这两个槽
		self.signal1.connect(self.sin1Call)
		self.signal1.connect(self.sin2Call)

		# 信号sin2连接到信号sin1
		self.signal2.connect(self.signal1)

        # 信号发射
		self.signal1.emit()
		self.signal2.emit(1)

		# 断开sin1、sin2信号与各槽的连接
		self.signal1.disconnect(self.sin1Call)
		self.signal1.disconnect(self.sin2Call)
		self.signal2.disconnect(self.signal1)

		# 信号sin1和sin2连接同一个槽sin1Call
		self.signal1.connect(self.sin1Call)
		self.signal2.connect(self.sin1Call)

        # 信号再次发射
		self.signal1.emit()
		self.signal2.emit(1)

	def sin1Call(self):
		print("signal-1 emit")

	def sin2Call(self):
		print("signal-2 emit")
  
if __name__ == '__main__':  
	signal = SignalClass()
