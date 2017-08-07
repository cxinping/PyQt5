# -*- coding: utf-8 -*- 
'''
    模块名：zwStrategy.py
    默认缩写：zwsta,示例：import zwStrategy as zwsta
   【简介】
    zwQT量化软件，策略分析模块库
     
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
#from pinyin import PinYin

from dateutil.parser import parse
from dateutil import rrule
import datetime as dt

#zwQuant
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zw_talib as zwta



#----策略函数    

    
#-----SMA策略 简单平均线策略        
def SMA_dataPre(qx,xnam0,ksgn0):    
    ''' 简单均线策略数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
            
    :ivar xcod (int): 股票代码
    '''
    
    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        d20['kprice']=d20['dprice'].shift(-1)
        #d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];d20=zwta.MA(d20,d,ksgn);
        d=qx.staVars[1];d20=zwta.MA(d20,d,ksgn);
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)      
        
def SMA_sta(qx):
    ''' 简单均线策略分析函数
        每次买100股
    Args:
        qx (zwQuantX): zwQuantX数据包
    默认参数示例：
        qx.staVars=[5,15,'2015-01-01','']      
 
 '''

    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=zwx.stkGetPrice(qx,'dprice')
    xnum=zwx.xusrStkNum(qx,xcod);
    #
    ksma='ma_%d' %qx.staVars[1]
    dsma=qx.xbarWrk[ksma][0]
    #
    if (dprice>dsma)and(xnum==0):
        stknum=100;
        #print('buy',xtim,dprice,dsma,xnum);
    if (dprice<=dsma)and(xnum>0):
        stknum=-1;
        #print('sell',xtim,dprice,dsma,xnum);
    #
    return stknum

def SMA20_dataPre(qx,xnam0,ksgn0):    
    ''' 简单均线策略数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
            
    :ivar xcod (int): 股票代码
    '''
    
    zwx.sta_dataPre0xtim(qx,xnam0);#print(qx.staVars)
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];d20=zwta.MA(d20,d,ksgn);
        d=qx.staVars[1];d20=zwta.MA(d20,d,ksgn);
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss) 
            
def SMA20_sta(qx):
    ''' 简单均线策略分析函数
        每次买90%的资金
    Args:
        qx (zwQuantX): zwQuantX数据包
    默认参数示例：
        qx.staVars=[5,15,'2015-01-01','']      
 
 '''

    stknum=0; 
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=zwx.stkGetPrice(qx,'dprice')
    xnum=zwx.xusrStkNum(qx,xcod);
    dcash=qx.qxUsr['cash'];
    #
    ksma='ma_%d' %qx.staVars[1]
    dsma=qx.xbarWrk[ksma][0]
    #
    if (dprice>dsma)and(xnum==0):
        stknum=int(dcash*qx.stkKCash/dprice);

        #print('buy',xtim,dprice,dsma,xnum);
    if (dprice<=dsma)and(xnum>0):
        stknum=-1;
        #print('sell',xtim,dprice,dsma,xnum);
    #
    return stknum
    
#-----CMA策略，cross MA 均线交叉策略

def CMA_dataPre(qx,xnam0,ksgn0):
    ''' 均线交叉策略数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        #---------------dprice,kprice
        #d20['dprice']=d20['open']*d20['adj close']/d20['close']
        d20['dprice']=d20[ksgn]
        d20['kprice']=d20['dprice']
        #d20['kprice']=d20['dprice'].shift(-1)
        #
        d=qx.staVars[0];d20=zwta.MA(d20,d,ksgn);k0ma='ma_%d' %qx.staVars[0]
        #d=qx.staVars[1];d20=zwta.MA(d20,d,ksgn);k1ma='ma_%d' %qx.staVars[1]
        #
        #d20['ma1n']=d20[k0ma].shift(1)
        d20['ma2n']=d20[k0ma].shift(2)
        
        #d20['dp1n']=d20['dprice'].shift(1)
        d20['dp2n']=d20['dprice'].shift(2)
        #---
        d20=np.round(d20,3);
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)
    
    
def CMA_sta(qx):
    ''' 均线交叉策略分析函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
    默认参数示例：
        qx.staVars=[30,'2014-01-01','']    
        '''

    stknum=0;
    xcod=qx.stkCode;
    dprice=zwx.stkGetPrice(qx,'dprice')
    dcash=qx.qxUsr['cash'];
    #duncash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    #----
    kmod=zwx.cross_Mod(qx)
    #
    if kmod==1: 
        if dnum0==0:
            stknum=int(dcash*qx.stkKCash/dprice);
    elif kmod==-1: 
        stknum=-1;
    #
    if stknum!=0:    
        #print(qx.xtim,stknum,'xd',xcod,dprice,dcash)    
        #print(kmod,qx.xtim,stknum,'xd',xcod,dprice,dcash)    
        #print('  ',stknum,dcash,qx.stkKCash,dprice)
        pass;
    
    return stknum    
    
#-------vwap策略，成交量加权平均价
        
def VWAP_dataPre(qx,xnam0,ksgn0):
    ''' 
    vwap 数据预处理函数,vwap策略，成交量加权平均价
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';'close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        #---------------dprice,kprice
        #d20['dprice']=d20['open']*d20['adj close']/d20['close']
        d20['dprice']=d20[ksgn]
        #d20['kprice']=d20['dprice'].shift(-1)
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['kprice']=d20['open'].shift(-1)
        #
        #d=qx.staVars[0];d20=zwta.MA(d20,d,ksgn);
        #d=qx.staVars[1];d20=zwta.MA(d20,d,ksgn);
        #
        #d20=zwta.MA(d20,qx.staMA_short,'adj close');
        #d20=zwta.MA(d20,qx.staMA_long,'adj close');
        #ksma='ma_'+str(qx.staMA_long);
        #d20['ma1n']=d20[ksma].shift(1)
        #d20['ma1n']=d20[ksma]
        #
        #---------------dprice,kprice
        #d20['dprice']=d20['open']*d20['adj close']/d20['close']
        
        #d20['dprice']=d20['adj close']
        #d20['kprice']=d20['dprice']
        #vwap,基于成交量的加权平均价
        #vwap = (prices * volume).sum(n) / volume.sum(n)  #sum函数自动忽略NaN值
        #vwapWindowSize,threshold
        #qx.staVarLst=[15,0.01]#
        nwin=qx.staVars[0];
        d20['vw_sum']=pd.rolling_sum(d20['dprice']*d20['volume'],nwin);
        d20['vw_vol']=pd.rolling_sum(d20['volume'],nwin);
        d20['vwap']=d20['vw_sum']/d20['vw_vol']
        
        #---
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)
    
       
def VWAP_sta(qx):
    ''' vwap 成交量加权平均价策略分析函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
    默认参数示例：
    qx.staVars=[5,0.01,'2014-01-01','']    
    '''

    
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    #
    vwap=zwx.stkGetPrice(qx,'vwap')
    if vwap>0:
        dprice=zwx.stkGetVars(qx,'close')
        kvwap=qx.staVars[1];
        xnum=zwx.xusrStkNum(qx,xcod);
        dcash=qx.qxUsr['cash'];
        dval = xnum * dprice;
        #----
        if (dprice>vwap*(1+kvwap))and(dval<(dcash*qx.stkKCash)):
            stknum=100;
        if (dprice<vwap*(1-kvwap))and(dval>0):
            stknum=-100;
        #
        if stknum!=0:    
            #print(xtim,stknum,'xd',xcod,dprice,dcash)    
            pass;
        
        
    return stknum            
#---BBANDS策略，布林带策略

       
def BBANDS_dataPre(qx,xnam0,ksgn0):
    ''' 布林带数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';'close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        #
        #d20['dprice']=d20['open']*d20['adj close']/d20['close']
        d20['dprice']=d20[ksgn]
        d20['kprice']=d20['dprice']
        #d20['kprice']=d20['dprice'].shift(-1)
        #d20['kprice']=d20['open'].shift(-1)
        #
        dnum=qx.staVars[0];
        d20=zwta.BBANDS_UpLow(d20,dnum,ksgn)
        #---
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)
    
def BBANDS_sta(qx):
    ''' 布林带策略分析函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
   默认参数示例：
   qx.staVars=[40,'2014-01-01','']    
   
   '''


    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dup=zwx.stkGetVars(qx,'boll_up')
    dlow=zwx.stkGetVars(qx,'boll_low')
    #print(xtim,stknum,'xd',xcod,dup,dlow)    
    if dup>0:
        dprice=zwx.stkGetPrice(qx,'dprice')
        kprice=zwx.stkGetPrice(qx,'kprice')
        dnum=zwx.xusrStkNum(qx,xcod)
        dcash=qx.qxUsr['cash'];
        #print(xtim,stknum,dnum,'xd',dcash,dprice,'b,%.2f,%.2f' %(dlow,dup))    
        if (dnum==0)and(dprice<dlow):
            stknum = int(dcash /dprice*qx.stkKCash);dsum=stknum*kprice
            if qx.debugMod>0:
                print(xtim,stknum,dnum,'++,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
        elif (dnum>0)and(dprice>dup):
            stknum = -1;dsum=dnum*kprice
            if qx.debugMod>0:
                print(xtim,stknum,dnum,'--,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            
        #
        if stknum!=0:    
            #print(xtim,stknum,'xd',xcod,dprice,dcash)    
            pass;
        
    return stknum
            
#---tur10海龟策略

def tur10(qx):
    '''
    海龟策略:deal_stock_num
    当今天的收盘价，大于过去n个交易日中的最高价时，以收盘价买入；
    买入后，当收盘价小于过去n个交易日中的最低价时，以收盘价卖出。
    deal_stock_num 是按资金总额的90% 购买股票
    默认参数示例：
    qx.staVars=[5,5,'2014-01-01','']    
    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    x9=qx.xbarWrk['xhigh'][0];
    x1=qx.xbarWrk['xlow'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    
    
    if dprice>x9:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (dprice<x1):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum    


def tur20(qx):
    '''
    海龟策略:deal_stock_num
    当今天的收盘价，大于过去n个交易日中的最高价时，以收盘价买入；
    买入后，当收盘价小于过去n个交易日中的最低价时，以收盘价卖出。
    tur20 是按，策略指定的数目 购买股票
    默认参数示例：
    qx.staVars=[5,5,'2014-01-01','']  
    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    x9=qx.xbarWrk['xhigh'][0];
    x1=qx.xbarWrk['xlow'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    knum0=qx.staVars[2]  #策略指定的数目,购买股票
    
    
    if dprice>x9:
        if dnum0==0:
            #stknum = int(dcash*0.9 /dprice);#dsum=stknum*kprice
            stknum = knum0
    elif (dprice<x1):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum  
    
def tur10_dataPre(qx,xnam0,ksgn0):
    ''' 
    海龟策略:deal_stock_num, 数据预处理函数 说明
    当今天的收盘价，大于过去n个交易日中的最高价时，以收盘价买入；
    买入后，当收盘价小于过去n个交易日中的最低价时，以收盘价卖出。
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    #zwsta.zwx.sta_dataPre0xtim(qx,xnam0);
    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc=ksgn0,ksgn0;  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];ksgn='xhigh0';d20[ksgn]=pd.rolling_max(d20['high'],d)
        d=qx.staVars[1];ksgn='xlow0';d20[ksgn]=pd.rolling_min(d20['low'],d)
        d20['xhigh']=d20['xhigh0'].shift(1)
        d20['xlow']=d20['xlow0'].shift(1)
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)   
                  
#---------------MACD策略
                  
def macd10(qx):
    '''
     MACD策略01
     MACD称为指数平滑异同平均线
    当 macd>0，买入；
    当 macd<0，卖出
    默认参数示例：
    qx.staVars=[12,26,'2014-01-01','']    

    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    xk=qx.xbarWrk['macd'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    
    
    if xk>0:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (xk<0):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum    
      


def macd20(qx):
    '''
    MACD策略02
     MACD称为指数平滑异同平均线
    当 macd>macd_sign，买入；
    当 macd<macd_sign0，卖出
    默认参数示例：
    qx.staVars=[12,26,'2014-01-01','']   

    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    xk=qx.xbarWrk['macd'][0];
    x2=qx.xbarWrk['msign'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    
    
    if xk>x2:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (xk<x2):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum        

def macd10_dataPre(qx,xnam0,ksgn0):
    ''' 
    MACD策略, 数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc,qx.priceBuy=ksgn0,ksgn0,ksgn0  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];d2=qx.staVars[1];
        d20=zwta.MACD(d20,d,d2,'close');
        #d20['macd1n']=d20['macd'].shift(1)
        #d20['msign1n']=d20['msign'].shift(1)
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)   
            
#------------kdj策略

def kdj10(qx):
    '''
     KDJ策略10
     KDJ 指标，又称随机指标
    当 stok>90，买入；
    当 stok<10，卖出
    默认参数示例：
    qx.staVars=[9,'2014-01-01','']    

    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    #
    ksgn1,ksgn2='stok','stod'
    xk,xk2=qx.xbarWrk[ksgn1][0],qx.xbarWrk[ksgn2][0];
    
    
    if xk>90:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (xk<10):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum               

def kdj20(qx):
    '''
       KDJ策略20
     KDJ 指标，又称随机指标
    当 stok>stod,并且朝上，买入；
    当 stok>stod,并且朝下，卖出
    默认参数示例：
    qx.staVars=[9,'2014-01-01','']    

    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    #
    ksgn1,ksgn2='stok','stod'
    xk,xk2=qx.xbarWrk[ksgn1][0],qx.xbarWrk[ksgn2][0];
    nksgn1,nksgn2='stok1n','stod1n'
    nxk,nxk2=qx.xbarWrk[nksgn1][0],qx.xbarWrk[nksgn2][0];
    
    if (xk>xk2)and(nxk<=nxk2):
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif (xk<xk2)and(nxk>=nxk2):
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum               



def kdj10_dataPre(qx,xnam0,ksgn0):
    ''' 
     KDJ策略
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc,qx.priceBuy=ksgn0,ksgn0,ksgn0  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];#d2=qx.staVars[1];
        d20=zwta.STOD(d20,d,'close');
        d20['stod1n']=d20['stod'].shift(1)
        d20['stok1n']=d20['stok'].shift(1)
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)  
                        
#----------RSI策略

def rsi10(qx):
    '''
    RSI策略
    RSI相对强弱指标
    当 rsi>kbuy，一般是70，80，买入
    当 rsi<sell，一般是30，20，卖出
    默认参数示例：
    qx.staVars=[14,70,30,'2015-01-01','']    
    '''
    stknum=0;
    xtim,xcod=qx.xtim,qx.stkCode
    dprice=qx.xbarWrk['dprice'][0];
    dcash=qx.qxUsr['cash'];
    dnum0=zwx.xusrStkNum(qx,xcod)
    #
    d=qx.staVars[0];kstr1='rsi_{n}'.format(n=d)
    xk=qx.xbarWrk[kstr1][0]
    kbuy,ksell=qx.staVars[1],qx.staVars[2]
    
    if xk>kbuy:
        if dnum0==0:
            stknum = int(dcash*qx.stkKCash /dprice);#dsum=stknum*kprice
            #stknum = 500
            #print(xtim,stknum,dnum,'++b,%.2f,%.2f,%.2f,$,%.2f,%.2f' %(dprice,dlow,dup,kprice,dsum))    
            #print(xtim,stknum,'++xd',xcod,dprice,x9,x1)    
    elif xk<ksell:
            #stknum = -500
            stknum = -1
            #stknum = -1;dsum=dnum*kprice
            
    if stknum!=0:
        #print(xtim,stknum,'xd',xcod,dprice,x9,x1)    
        pass;
        
    return stknum        

def rsi10_dataPre(qx,xnam0,ksgn0):
    ''' 
    RSI策略, 数据预处理函数
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)：函数标签
        ksgn0 (str): 价格列名称，一般是'adj close'
        '''

    zwx.sta_dataPre0xtim(qx,xnam0);
    #----对各只股票数据，进行预处理，提高后期运算速度
    ksgn,qx.priceCalc,qx.priceBuy=ksgn0,ksgn0,ksgn0  #'adj close';
    for xcod in zw.stkLibCode:
        d20=zw.stkLib[xcod];
        
        #  计算交易价格kprice和策略分析采用的价格dprice,kprice一般采用次日的开盘价
        #d20['dprice']=d20['open']*d20[ksgn]/d20['close']
        #d20['kprice']=d20['dprice'].shift(-1)
        d20['dprice']=d20['close']
        d20['kprice']=d20['dprice']
        #
        d=qx.staVars[0];#d2=qx.staVars[1];
        d20=zwta.RSI(d20,d);
        #d20['macd1n']=d20['macd'].shift(1)
        #d20['msign1n']=d20['msign'].shift(1)
        #
        zw.stkLib[xcod]=d20;
        if qx.debugMod>0:
            print(d20.tail())    
            #---
            fss='tmp\\'+qx.prjName+'_'+xcod+'.csv'
            d20.to_csv(fss)   
                        