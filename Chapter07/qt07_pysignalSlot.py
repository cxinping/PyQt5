# -*- coding: utf-8 -*-

"""
    【简介】
    内置信号槽示例


"""


from PyQt5.QtCore import QObject , pyqtSignal

#信号对象
class QTypeSignal(QObject):
    #定义一个信号槽
	sendmsg = pyqtSignal( object)
      
	def __init__( self):
		super( QTypeSignal, self).__init__()
            
	def run( self):
        # 发射信号
		self.sendmsg.emit('Hello Pyqt5')
          
# 槽对象          
class QTypeSlot(QObject):
	def __init__( self):
		super( QTypeSlot, self).__init__()
    
   # 槽对象里的槽函数      
	def get(self, msg):
		print("QSlot get msg => " + msg)


if __name__ == '__main__':
	send = QTypeSignal()
	slot = QTypeSlot()
	print('--- 连接信号槽 ---')    
	send.sendmsg.connect( slot.get)
	send.run()
    
	print('--- 断开信号槽 ---')        
	send.sendmsg.disconnect( slot.get )
	send.run()   

