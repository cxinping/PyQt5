# -*- coding: utf-8 -*- 
'''
    模块名：zwBacktest.py
    默认缩写：zwbt,示例：import zwBacktest as zwbt
   【简介】
    zwQT量化软件，回溯测试模块
     
    zw量化，py量化第一品牌
    网站:http://www.ziwang.com zw网站
    py量化QQ总群  124134140   千人大群 zwPython量化&大数据 
     
    开发：zw量化开源团队 2016.04.01 首发
  
'''

import numpy as np
import math
import pandas as pd
import matplotlib as mpl
import matplotlib.gridspec as gridspec
# from pinyin import PinYin

from dateutil.parser import parse
from dateutil import rrule
import datetime as dt

# zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zw_talib as zwta

from numba import *


# -------------

# -------------    zw.Quant.BackTest

def bt_init(xlst, rdat, prjNam, money0=1000000):
    '''
    qt_init(qx,xlst,rdat):
        初始化zw量化参数，stk股票内存数据库等
    【输入】：
        xlst (list): 股票代码列表，例如：xlst=['aeti','egan','glng','simo']，xlst=['002739','300239']   
        rdat (str): 股票数据目录,可直接使用 zwDat的中美股票数据:\\zwdat\\cn\\Day\\，\\zwdat\\us\\Day\\，
        prjNam (str): 项目名称
        money0 (int): 启动资金，默认是：1000000(100w)
        
    【输出】：
        qx (zwQuantx): 程序化全局变量qx
        '''
    # qx=zw.zwQuantX('tur',1000000) #100w
    qx = zw.zwQuantX(prjNam, money0)  # 100w

    # ------设置各种价格模式：
    #    priceWrk，策略分析时，使用的股票价格，一般是：dprice，复权收盘价
    #    priceBuy，买入/卖出的股票价格，一般是：kprice，一般采用次日的复权开盘价
    #    priceCalc，最后结算使用的股票价格，一般是：adj close，复权收盘价
    qx.priceCalc = 'close'  # qx.priceCalc='adj close'
    qx.priceWrk = 'dprice'
    qx.priceBuy = 'kprice'
    # ----------设置绘图&数据输出格式
    mpl.style.use('seaborn-whitegrid')
    pd.set_option('display.width', 450)
    # -----设置数据源目录等场所，读取股票数据，stkLib
    qx.rdat = rdat
    zwx.stkLibRd(xlst, rdat)
    #
    # 大盘指数.设置
    # zw.stkInxLib=None  #全局变量，大盘指数，内存股票数据库
    qx.stkInxRDat = '\\zwdat\\cn\\xday\\'  # 大盘指数数据源路径
    qx.stkInxPriceName = 'close'  # 大盘指数数据列名称，默认是:close
    # 大盘指数代码,名称拼音,中文名称
    # qx.stkInxCode,qx.stkInxName,qx.stkInxCName='000001','sh001','上证指数'

    #  读取股票数据，
    xtim0 = parse('9999-01-01')
    xtim9 = parse('1000-01-01')
    zw.stkLibTim = {}  # 记录每只股票的交易起点时间和终点时间，终点作为清仓判断标志。
    for xcod in zw.stkLibCode:
        xt0, xt9 = zwx.stkLibGetTimX(xcod)
        xcod_tim0 = xt0.strftime('%Y-%m-%d')
        xcod_tim9 = xt9.strftime('%Y-%m-%d')
        zw.stkLibTim[xcod] = [xcod_tim0, xcod_tim9]
        if xtim0 > xt0: xtim0 = xt0
        if xtim9 < xt9: xtim9 = xt9

    xtim0 = xtim0.strftime('%Y-%m-%d')
    xtim9 = xtim9.strftime('%Y-%m-%d')
    qx.qxTimSet(xtim0, xtim9)

    if qx.debugMod > 0:
        print(xtim0, xtim9, '\nstkCode', zw.stkLibCode)  # zwx.stkLibPr()

    return qx


def zwBackTest100(qx):
    '''
    zwBackTest100(qx):
    zwQT回溯测试子函数，测试一只股票xcod，在指定时间xtim的回溯表现数据
    会调用qx.staFun指定的策略分析函数，获取当前的股票交易数目 qx.stkNum
    并且根据股票交易数目 qx.stkNum，判定是不是有效的交易策略
    【输入】
        qx (zwQuantx): zwQuantx数据包
        #qx.stkCode，当前交易的股票代码
        #qx.xtim，当前交易的时间
    【输出】
         无
         '''

    # ----运行策略函数，进行策略分析
    qx.stkNum = qx.staFun(qx)
    # ----
    if qx.stkNum != 0:
        # ----检查，是不是有效交易
        xfg, qx.xtrdChk = zwx.xtrdChkFlag(qx)
        if xfg:
            # ----如果是有效交易，加入交易列表
            zwx.xtrdLibAdd(qx)
            # qx.prQCap()
        elif qx.trdNilFlag:
            zwx.xtrdLibNilAdd(qx)


def zwBackTest(qx):
    '''
    zwQuant，回溯测试主程序
    【输入】
    	qx (zwQuantx): zwQuantx数据包
    	
    【输出】
         无
         '''
    # 增加数据源波动率参数  # 就是增加一列dvix数据
    zwx.stkLibSetDVix()
    # 计算回溯时间周期，也可以在此，根据nday调整回溯周期长度
    # 或者在 qt_init数据初始化时，通过qx.qxTimSet(xtim0,xtim9)，设置回溯周期长度
    nday = qx.periodNDay
    if qx.debugMod > 0:
        xcod = zw.stkLibCode[0]
        print(zw.stkLib[xcod].tail())
        print('nday', nday)
        fss = 'tmp\\' + qx.prjName + '_' + xcod + '.csv'
        zw.stkLib[xcod].to_csv(fss)
        # --------------
    # 按时间循环，进行回溯测试
    for tc in range(nday):
        tim5 = qx.DTxtim0 + dt.timedelta(days=tc)
        if hasattr(qx,'timFun'):
            qx.timFun(qx,tim5)  # 运行绑定的关于某个时间点的主函数

        xtim = tim5.strftime('%Y-%m-%d')  # print('tc',tc,xtim)
        # 每个测试时间点，开始时，清除qx相关参数
        qx.qxTim0SetVar(xtim)  # qx.prQxUsr() #qx.xtim=xtim
        xpriceFlag = False  # 有效交易标志Flag
        # 按设定的股票代码列表，循环进行回溯测试
        for xcod in zw.stkLibCode:
            qx.stkCode = xcod  # print('xcod',xcod)
            # xdatWrk是当前xcod，=stkLib[xcod]
            # xbarWrk是当前时间点的stkLib[xcod]
            # 注意,已经包括了，qt_init里面的扩充数据列
            qx.xbarWrk, qx.xdatWrk = zwx.xbarGet8TimExt(xcod, qx.xtim)
            # print(xcod,'xbar\n',qx.xbarWrk)
            if not qx.xbarWrk[qx.priceWrk].empty:
                # -----dvix 波动率检查
                dvix = zwx.stkGetVars(qx, 'dvix')  # dvixFlag=False
                dvixFlag = zwt.xinEQ(dvix, qx.dvix_k0, qx.dvix_k9) or (dvix == 0) or (np.isnan(dvix))
                if dvixFlag:
                    xpriceFlag = True
                    # 调用回溯子程序，如果是有效交易，设置成功交易标志xtrdFlag
                    zwBackTest100(qx)
                else:
                    print('@dvix', xcod, xtim, dvix)
                    pass

        # 如果所有股票代码列表循环完毕，成功交易标志为真
        # 在当前测试时间点终止，设置有关交易参数
        if xpriceFlag:
            qx.wrkNDay += 1
            qx.qxTim9SetVar(qx.xtim)
    # print('')
    qx.update_usr_qxLib(qx,qx.qxLib)
    # print('')
    # print('')
    # print('')
    # print('')



if __name__ == '__main__':
    import line_profiler
    import sys

    prof = line_profiler.LineProfiler(bt_init)
    prof.enable()  # 开始性能分析
    xlst = ['orcl-2000']
    bt_init(xlst, 'dat\\', 'sma', 10000)
    prof.disable()  # 停止性能分析
    prof.print_stats(sys.stdout)


    # if 'builtins' not in dir() or not hasattr(builtins, 'profile'):
    #     import builtins
    #     def profile(func):
    #         def inner(*args, **kwargs):
    #             return func(*args, **kwargs)
    #         return inner
    #     builtins.__dict__['profile'] = profile
