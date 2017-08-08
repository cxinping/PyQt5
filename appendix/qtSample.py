# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication( )  
w = QWidget()
w.resize(350,300)
w.setWindowTitle('PyQt5 从入门到实战')
w.show()

sys.exit(app.exec_())
