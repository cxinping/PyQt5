# -*- coding: utf-8 -*- 
'''
    【简介】
	保存PyQt5类的使用手册到本地
   
    
'''

import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'E:\QWidget.txt' , 'w')
help( QTableWidget )
sys.stdout.close()
sys.stdout = out
