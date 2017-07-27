# -*- coding: utf-8 -*- 
'''
    【简介】
	保存PyQt5类的使用手册到本地
   
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage 
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'E:\QWidget.txt' , 'w')
help( QWidget  )
sys.stdout.close()
sys.stdout = out
