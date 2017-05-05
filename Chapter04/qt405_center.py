# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QWidget , QApplication 
import sys  
    
class Winform( QWidget): 
    
    def __init__(self, parent=None):
        super( Winform, self).__init__(parent)
          
        self.setWindowTitle('窗口居中例子')  
        self.resize(350,  250)  
        self.center()  
          
    def center(self):  
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()        
        self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)  
  
if __name__ == "__main__": 
    app = QApplication(sys.argv)   
    win = Winform()  
    win.show()  
    sys.exit(app.exec_())  
