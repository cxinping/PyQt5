# -*- coding: utf-8 -*-

"""
    【简介】
    内置信号槽示例


"""


from PyQt5.QtCore import QObject , pyqtSignal

class QTypeSignal(QObject):
      sendmsg = pyqtSignal( object)
      
      def __init__( self):
          QObject.__init__( self)
          
      def run( self):
          self.sendmsg.emit('发射信号 ')
          
          
class QTypeSlot(QObject):
      def __init__( self):
          QObject.__init__( self)
          
      def get(self, msg):
          print("Qslt get msg => " + msg)


if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()
    send.sendmsg.connect( slot.get)
    send.run()

