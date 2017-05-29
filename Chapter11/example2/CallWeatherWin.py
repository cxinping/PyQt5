# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_Form

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):    
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
            
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    win = MainWindow()  
    win.show()  
    sys.exit(app.exec_())  
