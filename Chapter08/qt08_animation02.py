# -*- coding: utf-8 -*-

"""
    【简介】
   
    
    
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()
animation = QPropertyAnimation(window, b"geometry")
animation.setDuration(10000)
animation.setStartValue(QRect(0, 0, 100, 30))
#animation.setKeyValueAt(0.5, QRect(240, 240, 100, 30));
animation.setEndValue(QRect(250, 250, 100, 30))
# animation.setEasingCurve(QEasingCurve.OutBounce)
animation.start()

sys.exit(app.exec_())
