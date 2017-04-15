# -*- coding: utf-8 -*-

import time
import os

if __name__ == '__main__' :   
   for i in range(5): 
       os.system("python openweb.py")
       print("正在刷新页面. 次数 =>" ,  i)
       time.sleep(10)


