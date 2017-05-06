# -*- coding: utf-8 -*-

"""
    【简介】
     动画分组
    
    
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()
window2 = QMainWindow()
window2.show()

animation = QPropertyAnimation(window, b"geometry")
animation2 = QPropertyAnimation(window2, b"geometry")

group = QParallelAnimationGroup()

animation.setDuration(10000)
animation.setStartValue(QRect(0, 0, 100, 30))
animation.setEndValue(QRect(250, 250, 100, 30))
animation.setEasingCurve(QEasingCurve.OutBounce)

animation2.setDuration(10000)
animation2.setStartValue(QRect(250, 150, 100, 30))
animation2.setEndValue(QRect(850, 250, 100, 30))
animation2.setEasingCurve(QEasingCurve.CosineCurve)

group.addAnimation(animation)
group.addAnimation(animation2)
group.start()

sys.exit(app.exec_())
