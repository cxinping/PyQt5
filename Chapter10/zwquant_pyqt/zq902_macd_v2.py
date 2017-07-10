# -*- coding: utf-8 -*-
  


import numpy as np
import pandas as pd

#zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zwStrategy as zwsta
import zw_talib as zwta

#=======================    

    
def bt_endRets(qx):
    #---ok ，测试完毕
    # 保存测试数据，qxlib，每日收益等数据；xtrdLib，交易清单数据
    #qx.qxLib=qx.qxLib.round(4)
    qx.qxLib.to_csv(qx.fn_qxLib,index=False,encoding='utf-8')
    qx.xtrdLib.to_csv(qx.fn_xtrdLib,index=False,encoding='utf-8')
    qx.prQLib()
    #
    #-------计算交易回报数据
    zwx.zwRetTradeCalc(qx)
    zwx.zwRetPr(qx)



    print('')
    print('每日交易推荐')
    print('::xtrdLib',qx.fn_xtrdLib)
    print(qx.xtrdLib.tail())
    #print(qx.xtrdLib)


    # 使用自定义输出结果
    if qx.pyqt_mode_flag == True:
        zwdr.my_pyqt_show(qx)
    else:
        zwdr.my_qunt_plot(qx)


#==================main
#--------init，设置参数
rss='dat\\'  #rss='\\zwdat\\cn\\day\\'
xlst=['600401']   #600401,*ST海润
qx=zwbt.bt_init(xlst,rss,'macd20',10000)

#---设置策略参数
qx.staVars=[12,26,'2015-01-01','']    
qx.debugMod=1
qx.pyqt_mode_flag = True
qx.staFun=zwsta.macd20 #---绑定策略函数&运行回溯主函数

#---根据当前策略，对数据进行预处理
zwsta.macd10_dataPre(qx,'macd20','close')
#----运行回溯主程序

zwbt.zwBackTest(qx)
#----输出回溯结果
bt_endRets(qx) #
    
