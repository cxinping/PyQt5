# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication

from Ui_MainWinSignalSlog04 import Ui_MainWindow

#注：原代码为 from .Ui_MainWinSignalSlog04 import Ui_MainWindow，运行出错，需要去掉.

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(True) # 设置checkBox默认的初始状态为选择

    
    @pyqtSlot(bool)
    def on_checkBox_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.label.setVisible(checked)
        self.lineEdit.setEnabled(checked)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())