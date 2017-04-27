# -*- coding: utf-8 -*-

"""
    【简介】
    信号和槽的自动连接例子
    
    
"""

from PyQt5 import QtCore 
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton
import sys
    
    
class CustWidget( QWidget):
    
    def __init__(self, parent=None):
        super(CustWidget, self).__init__(parent)
        
        self.ok_button = QPushButton("OK", self)
        self.ok_button.setObjectName("ok_button")
        
        layout =  QHBoxLayout()
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    @QtCore.pyqtSlot()    
    def on_ok_button_clicked(self):
        print( "OK")
        
        
if __name__ == "__main__":        

    app =  QApplication(sys.argv)
    w = CustWidget()
    w.show()
    app.exec_()
