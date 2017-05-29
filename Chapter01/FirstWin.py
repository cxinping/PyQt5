# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)    
    btn = QPushButton("Hello PyQt5")
    btn.clicked.connect(QCoreApplication.instance().quit)
    btn.resize(400,100)
    btn.move(50,50)
    btn.show()

    sys.exit(app.exec_())
