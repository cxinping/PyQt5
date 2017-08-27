# -*- coding: utf-8 -*- 
'''
  
  zwQuantToolBox 2016
  zw量化开源工具箱系列软件 
  http://www.ziwang.com,Python量化第一品牌 
  
  文件名:zwQTBox.py
  说明：import zwQTBox as zwx
  常用zwQuant量化工具函数集
  

'''

import sys, os
import numpy as np
import tushare as ts
import pandas as pd
#import pandas_datareader.data as web

from numba import *

import csv
import pickle
from datetime import *
from dateutil.parser import parse
from dateutil import rrule
import datetime as dt

import zwSys as zw  #::zwQT
import zwTools as zwt


# -------------

# -------------xtick tick分笔数据下载



def xtick_down_init(qx, finx):
    '''
    根据finx股票代码文件名，读取数据到qx.stkCodeLib
    并根据预设的日期，初始化相关的时间参数
    [输入]
        qx.xdayNum,下载时间周期为0，采用指定下载起始、结束日期模式
            qx.xday0k，数据下载起始日期，为空使用默认起始日期：2005-01-01
            qx.xday9k，数据下载结束日期，为空使用当前日期
            日期为字符串格式，'yyyy-mm-dd'
        qx.xdayNum,下载时间周期大于0时，采用指定时间周期模式，一般用于数据追加
            #数据追加模式，无需设置起始、结束日期，
            例如，qx.xdayNum=2  #下载今天以前2天的数据，注意这个是日历间隔，不是工作日间隔
    '''
    # ---finx
    qx.fn_stkCode = finx
    print(finx)
    qx.stkCodeLib = pd.read_csv(finx, encoding='gbk')
    qx.codeNum = len(qx.stkCodeLib['code'])
    # ---xtim0 qx.xday0k,qx.xday9k='2010-01-01','' qx.xday0k,qx.xday9k='',''
    if qx.xdayNum > 0:
        qx.DTxtim9 = dt.datetime.now()
        qx.DTxtim0 = qx.DTxtim9 - dt.timedelta(days=qx.xdayNum)
    else:
        if qx.xday9k == '':
            qx.DTxtim9 = dt.datetime.now()
        else:
            qx.DTxtim9 = parse(qx.xday9k)
        if qx.xday0k == '':
            qx.DTxtim0 = dt.datetime.now()
        else:
            qx.DTxtim0 = parse(qx.xday0k)
        #
        # qx.DTxtim9=zwt.iff2(qx.xday9k=='',dt.datetime.now(),parse(qx.xday9k))
        # qx.DTxtim0=zwt.iff2(qx.xday0k=='',qx.DTxtim9+dt.timedelta(days=-2) ,parse(qx.xday0k))
        #
        qx.xdayNum = rrule.rrule(rrule.DAILY, dtstart=qx.DTxtim0, until=qx.DTxtim9).count()
    #

    qx.xtim0Sgn, qx.xtim9Sgn = qx.DTxtim0.strftime('%Y-%m-%d'), qx.DTxtim9.strftime('%Y-%m-%d')
    print('\n@nday', qx.xdayNum, qx.xtim0Sgn, '@', qx.xtim9Sgn)  # nday=13


def xtick_down100(qx, ftg):
    '''
    根据指定的日期，股票代码，数据文件名：ftg
    下载指定股票指定日期的ticks数据，并保存到ftg
    [输入]
        qx.code，股票代码
        qx.xtimSgn，当前日期的字符串
        ftg，保存tick数据的文件名
    '''
    df, dn = [], 0
    try:
        df = ts.get_tick_data(qx.code, date=qx.xtimSgn)  # print(df.head())
    except IOError:
        pass  # skip,error
    datFlag, dn = False, len(df)
    print('     n', dn, ftg)  # 跳过无数据 日期
    # if zwt.xin(dn,0,9):print('n2',dn,ftg)
    if dn > 10:
        df['type'] = df['type'].str.replace(u'中性盘', 'norm')
        df['type'] = df['type'].str.replace(u'买盘', 'buy')
        df['type'] = df['type'].str.replace(u'卖盘', 'sell')
        df.to_csv(ftg, index=False, encoding='utf')
        datFlag = True
    #
    return datFlag, dn


def xtick_down8tim_codes(qx):
    '''
    下载指定日期，stkCodeLib包含的所有代码的tick历史分笔数据
    并转换成对应的分时数据：5/15/30/60 分钟
    数据文件保存在：对应的数据目录 \zwdat\tick\yyyy-mm\
        目录下，yyyy，是年份；mm，是月份
    运行时，会根据日期，股票代码，生成数据文件名：ftg
    [输入]
      qx.xtimSgn，当前日期的字符串
      qx.stkCodeLib，包含所有股票代码的pd数据表格
          '''
    # qx.xday0ChkFlag=False self.codeInx0k=-1
    # inx0,qx.codeNum=qx.codeInx,len(dinx['code'])
    numNil = 0
    for i, xc in enumerate(qx.stkCodeLib['code']):
        code = "%06d" % xc  # print("\n",i,"/",qx.codeNum,"code,",code)
        qx.code, qx.codeCnt = code, i
        # ---
        ftg = '%s%s_%s.csv' % (qx.rtickTimMon, code, qx.xtimSgn)
        xfg = os.path.exists(ftg)
        if xfg:
            numNil = 0
        else:
            if numNil < 90:
                datFlag, dfNum = xtick_down100(qx, ftg)
                numNil = zwt.iff2(datFlag, 0, numNil + 1)
                if dfNum == 3: numNil += 10
            #
            print(xfg, datFlag, qx.codeCnt, "/", qx.codeNum, ftg, numNil)
        #
        if numNil > 90: break
        # if i>3:break


def xtick_down8tim_all(qx, finx):
    '''
    下载所有股票代码的所有tick历史分笔数据，按时间日期循环下载
    数据文件保存在：对应的数据目录 \zwdat\tick\yyyy-mm\
        目录下，yyyy，是年份；mm，是月份
    [输入]
      finx，股票代码文件
          '''

    xtick_down_init(qx, finx)
    # qx.xday0ChkFlag=False
    print('r', qx.rdat, qx.rtickTim)
    #    self.rtickTimMon=self.rtickTim+'2010-01\\'  #   \zwDat\ticktim\  2012-01\
    for tc in range(qx.xdayNum):
        qx.DTxtim = qx.DTxtim0 + dt.timedelta(days=tc)
        qx.xdayInx, qx.xtimSgn = tc, qx.DTxtim.strftime('%Y-%m-%d')
        #
        rmon0 = qx.DTxtim.strftime('%Y-%m')
        qx.rtickTimMon = '%s%s\\' % (qx.rtickTim, rmon0)
        xfg = os.path.exists(qx.rtickTimMon)
        if not xfg:
            os.mkdir(qx.rtickTimMon)
        #
        print('\n', xfg, qx.xdayInx, '/', qx.xdayNum, qx.xtimSgn)
        #
        xtick_down8tim_codes(qx)


# ----xtimck2tim.xxx 分笔tick数据，转换为分时数据




def xtick2tim_code010(qx):
    '''
    根据指定的股票代码，
    把所有tick历史分笔数据
    转换成对应的分时数据：5/15/30/60 分钟
    数据文件保存在：对应的数据目录 \zwdat\min\
    [输入]
      qx.code，股票代码
      qx.min_ksgns,分时数据时间模式列表，一般是[5，15，30，60]，也可以自行设置
      self.xtickAppendFlag=False
    '''
    # xtick_setTimeDat(qx)

    for kss in qx.min_ksgns:
        rx.min_knum, rx.min_ksgnWrk = int(kss), 'M' + kss
        qx.datMin[kss] = pd.DataFrame(columns=zw.qxMinName)
        # 默认=False，tick数据追加模式标志,如果=True,强行将所有tick文件转换为分时数据
        if qx.xtickAppFlag:

            fss = zw._rdatTick + qx.code + '\\' + qx.xtim + '.csv'
            xfg = os.path.exists(fss)
            if xfg: qx.datMin[ksgn] = pd.read_csv(fss, index_col=False)
    #
    flst = os.listdir(zw._rdatTick + qx.code + '\\')
    qx.codeCnt, qx.codeNum = 0, len(flst)
    for fs0 in flst:
        qx.codeCnt += 1
        nday = qx.codeNum - qx.codeCnt
        if (not qx.xtickAppFlag) or (nday < qx.xtickAppNDay):
            qx.xtim = fs0.split('.')[0]
            xtick2tim100(qx)
            print(qx.codeCnt, "/", qx.codeNum, qx.xtim, nday, qx.xtickAppNDay, qx.xtickAppFlag, '@', qx.code)
            #

    # ---------wr.code分时数据
    xtick2minWr(qx, zw._rdatTick)


# ---------

def xtick2minWr(qx, rsk):
    '''
    把所有分时数据，保存到文件
    会自动去重
    对应的数据目录 \zwdat\min\
        输出数据在min目录对应的分时目录当中，已经自动转换为5,15,30,60分钟分时数据
    
    '''
    print(qx.min_ksgns)
    for ksgn0 in qx.min_ksgns:
        sgnMin = 'M' + ksgn0
        xdf = qx.datMin[sgnMin]
        xdf.drop_duplicates(subset='time', keep='last', inplace=True)
        xdf = np.round(xdf, 2)
        xdf = xdf.sort_values(by=['time'], ascending=False)
        # fss=zw._rdatMin+sgnMin+'\\'+qx.code+'.csv' # print(fss)
        fss = rsk + sgnMin + '\\' + qx.code + '.csv'
        print(fss)
        if len(xdf) > 3:
            xdf.to_csv(fss, columns=zw.qxMinName, index=False, encoding='utf')
        qx.datMin[sgnMin] = xdf


def xtick2minsub(df):
    '''
    tick 数据 转换值程序，
    对根据qx.minType切割的数据，进行汇总，
    tick 数据 转换为分时数据：5/15/30/60 分钟
    输入
        df，根据qx.minType切割的数据
    输出
        ds，汇总后的数据，注意，格式是：pd.Series
    '''
    ds = pd.Series(index=zw.qxMinName)
    x9 = df.iloc[-1]
    ds['open'] = x9['price']
    x0 = df.iloc[0]
    ds['close'] = x0['price']
    #
    ds['high'], ds['low'] = np.max(df['price']), np.min(df['price'])
    ds['volume'], ds['amount'] = np.sum(df['volume']), np.sum(df['amount'])
    #
    xlst = ['norm', 'buy', 'sell']
    for xsgn in xlst:
        df2 = df[df['type'] == xsgn]
        if len(df2) > 0:
            ds['vol_' + xsgn], ds['amo_' + xsgn] = np.sum(df2['volume']), np.sum(df2['amount'])
        else:
            ds['vol_' + xsgn], ds['amo_' + xsgn] = 0, 0
    #
    return ds


def xtick2min010(qx):
    '''
       将下载的tick分笔数据，转换为分时数据：5/15/30/60 分钟
       并且追加到对应的分时数据列表当中
       注意qx.xtimTick0,qx.xtimTick9是预设时间数据，在zwDatX类定义并初始化
       输入
           qx.min_ksgnWrk
           qx.min_knum
           
    '''

    wrkDTim0, dt9 = parse(qx.xtimTick0), parse(qx.xtimTick9)
    xt = dt9 - wrkDTim0
    numMin = xt.total_seconds() / 60
    xn9 = int(numMin / qx.min_knum) + 1  # print(wrkDTim0,xn9) #xn9=7
    for tc in range(xn9):
        wrkDTim9 = wrkDTim0 + dt.timedelta(minutes=qx.min_knum)
        strTim0, strTim9 = wrkDTim0.strftime('%H:%M:%S'), wrkDTim9.strftime('%H:%M:%S')
        # ---cut tick.dat by tim
        df = qx.datTick  # print(df.head())
        df2 = df[df['time'] < strTim9]
        df3 = df2[df2['time'] >= strTim0]
        if len(df3) > 0:
            # -----tick 数据 转换为分时数据：5/15/30/60 分钟
            ds = xtick2minsub(df3)
            ds['time'] = qx.xtimSgn + ' ' + strTim0
            qx.datMin[qx.min_ksgnWrk] = qx.datMin[qx.min_ksgnWrk].append(ds.T, ignore_index=True)
        # ----ok,#tc
        wrkDTim0 = wrkDTim9


def xtick2tim100(qx, fdat):
    '''
    根据输入的fdat文件名，读取tick分笔数据，并转换为对应的分时数据：5/15/30/60 分钟
    【输入】
    fdat，rick数据文件名
    
    '''
    xfg = os.path.exists(fdat)  # print('x100',xfg,fdat)
    if xfg:
        qx.datTick = pd.read_csv(fdat, index_col=False)
        if len(qx.datTick) > 10:
            for kss in qx.min_ksgns:  # qx.min_ksgns=['M05','M15','M30','M60']
                qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
                xtick2min010(qx)


def xtick2tim_nday(qx):
    '''
    将指定时间周期的tick数据，转换为分时数据
          '''
    for tc in range(qx.xdayNum):
        qx.DTxtim = qx.DTxtim0 + dt.timedelta(days=tc)
        qx.xdayInx, qx.xtimSgn = tc, qx.DTxtim.strftime('%Y-%m-%d')
        #
        rmon0 = qx.DTxtim.strftime('%Y-%m')
        qx.rtickTimMon = '%s%s\\' % (qx.rtickTim, rmon0)
        fdat = '%s%s_%s.csv' % (qx.rtickTimMon, qx.code, qx.xtimSgn)
        #
        print(qx.xdayInx, '/', qx.xdayNum, qx.xtimSgn, fdat)
        xtick2tim100(qx, fdat)


def xtick2tim_code100(qx):
    '''
    根据qx.min_ksgns预设的分时参数，
    以及指定的股票代码、时间周期参数，
    将对应的tick数据，转换为分时数据，并保存到文件
    【输入】
        qx.code，股票代码
        qx.min_ksgns,分时数据时间模式列表，一般是[5，15，30，60]，也可以自行设置
    【输出】
       分时数据保存在目录：
           \zwdat\min\Mxx\
    '''
    for kss in qx.min_ksgns:
        qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
        qx.rminWrk = '%s\\%s\\' % (qx.rmin0k, qx.min_ksgnWrk)
        if not os.path.exists(qx.rminWrk): os.mkdir(qx.rminWrk)
        #
        qx.datMin[ksgn] = pd.DataFrame(columns=zw.qxMinName)
        fss = '%s%s.csv' % (qx.rminWrk, qx.code)  # print('@fss',fss,len(qx.datMin[ksgn]))
        xfg = os.path.exists(fss)  # print(xfg,'@f100',fss,len(qx.datMin[ksgn]))
        if xfg:
            qx.datMin[ksgn] = pd.read_csv(fss, index_col=False)
            print('\n@fss', fss, len(qx.datMin[ksgn]))
    #
    xtick2tim_nday(qx)
    xtick2minWr(qx, qx.rmin0k)


def xtick2tim_allcode(qx):
    '''
    将所有股票代码的tick数据转换为分时数据
    输入：
        qx.stkCodeLib:，股票代码列表文件，
        qx.min_ksgns,分时数据时间模式列表，一般是[5，15，30，60]，也可以自行设置
    输出
        \zwdat\min\
        输出数据在tick目录对应的分时目录当中，已经自动转换为5,15,30,60分钟分时数据
        为当天最新实时分笔数据，会自动覆盖以前的就数据
    '''
    for i, xc in enumerate(qx.stkCodeLib['code']):
        code = "%06d" % xc  # print("\n",i,"/",qx.codeNum,"code,",code)
        qx.code, qx.codeCnt = code, i
        print(qx.codeCnt, "/", qx.codeNum, qx.rtickTimMon, code, qx.xtimSgn)
        #
        xtick2tim_code100(qx)


# ---------------xtick.real.xxx

def xtick_real_downsub(xcod):
    ''' 中国A股,tick 历史或real实时 tick 分笔数据下载子程序
        会自动将中文type，替换成 英文：中性盘：norm；买盘：buy 卖盘：sell
        
    【输入】
        xcod,股票代码
        xtim，日期字符串，当xtim为空时，下载的是当天 实时 tick数据
    【输出】
        df,股票 tick  数据
            数据列格式：
            time,price,change,volume,amount,type
    '''
    xd = ts.get_today_ticks(xcod)
    dn = len(xd)  # print('n',dn) # 跳过无数据 日期
    if dn > 10:
        xd['type'] = xd['type'].str.replace(u'中性盘', 'norm')
        xd['type'] = xd['type'].str.replace(u'买盘', 'buy')
        xd['type'] = xd['type'].str.replace(u'卖盘', 'sell')
        # xd.to_csv('tmp\\'+xcod+'_'+xtim+'.csv',index=False,encoding='utf')
    else:
        xd = []
    #
    return xd


def xtick_real_down_all(qx, finx):
    '''
    下载当天的实时tick分笔数据，并自动转换为分时数据
    输入：
        finx，股票目录索引文件，一般每个股票，下载需要2-3分钟，
            如果做高频。单机股票代码不要太多，可以分组在多台电脑运行
        qx.min_ksgns，股票分时参数，例如：['20','60']
    输出
        \zwdat\tickreal\ 输出目录
        \zwdat\tickreal\tick\ 分笔tick数据
        \zwdat\tickreal\Mxx\ 分笔tick数据，转换后的分时数据
        
        输出数据在对应的tick目录当中，已经自动转换为分时数据
        当天最新实时tikc、分笔数据，会自动覆盖以前的旧数据
        
        
    '''
    # qx.min_ksgns=['05','15','30','60']
    rdat = zw._rdatTickReal
    dinx = pd.read_csv(finx, encoding='gbk')
    print('finx', finx)
    i, xn9 = 0, len(dinx['code'])
    for xc in dinx['code']:
        i += 1
        code = "%06d" % xc
        qx.codeCnt, qx.code = i, code
        print("\n", i, "/", xn9, "code,", code)
        # ---
        df = xtick_real_downsub(code)
        if len(df) > 10:
            fss = rdat + 'tick\\' + qx.code + '.csv'
            print('\n', fss)
            df.to_csv(fss, index=False, encoding='utf')
            qx.datTick = df
            # ---------- tick 分笔数据，转换为分时数据：05,15,30,60
            for kss in qx.min_ksgns:  # qx.min_ksgns=['M05','M15','M30','M60']
                qx.min_knum, qx.min_ksgnWrk, ksgn = int(kss), 'M' + kss, 'M' + kss
                qx.rminWrk = '%s\\%s\\' % (qx.rmin0k, qx.min_ksgnWrk)
                if not os.path.exists(qx.rminWrk): os.mkdir(qx.rminWrk)
                #
                # sgnMin='M'+ksgn0 # qx.minType=int(ksgn0)       # print('@mt',qx.minType)
                qx.datMin[ksgn] = pd.DataFrame(columns=zw.qxMinName)
                xtick2min010(qx)
                #
            xtick2minWr(qx, rdat)


# ----------------down.stk

def down_stk_cn020inx(qx, xtim0):
    ''' 下载大盘指数数据,简版股票数据，可下载到1994年股市开市起
    【输入】
        qx.xcod:指数代码

    '''
    xcod = qx.code
    tim0 = xtim0  # tim0='1994-01-01'
    xd = []
    rss = qx.rXDay
    fss = rss + xcod + '.csv'
    # if ((xtyp!='D')and(xtyp!='9') ):    tim0=tim0+" 00:00:00"

    # -------------------
    xfg = os.path.exists(fss)
    xd0 = []
    if xfg:
        xd0 = pd.read_csv(fss, index_col=0, parse_dates=[0], encoding='gbk')
        # print(xd0.head())
        xd0 = xd0.sort_index(ascending=False)
        # tim0=xd0.index[0]
        _xt = xd0.index[0]  # xt=xd0.index[-1]###
        s2 = str(_xt)
        tim0 = s2.split(" ")[0]

    #
    print('\n', xfg, fss, ",", tim0)
    # -----------
    try:
        xd = ts.get_h_data(xcod, start=tim0, index=True, end=None, retry_count=5, pause=1)  # Day9
        # -------------
        if xd is not None:
            if (len(xd0) > 0):
                xd2 = xd0.append(xd)
                #  flt.dup 
                xd2["index"] = xd2.index
                xd2.drop_duplicates(subset='index', keep='last', inplace=True)
                del (xd2["index"])
                # xd2.index=pd.to_datetime(xd2.index)
                xd = xd2

            xd = xd.sort_index(ascending=False)
            xd = np.round(xd, 3)
            xd.to_csv(fss, encoding='gbk')
    except IOError:
        pass  # skip,error

    return xd


def down_stk_cn010(qx):
    ''' 中国A股数据下载子程序
    【输入】
        qx (zwDatX): 
        xtyp (str)：数据类型，9,Day9,简版股票数据，可下载到2001年，其他的全部是扩充版数据，只可下载近3年数据
            D=日k线 W=周 M=月 默认为D
    :ivar xcod (int): 股票代码
    :ivar fss (str): 保存数据文件名
    '''

    xcod, rss, = qx.code, qx.rDay
    tim0 = '1994-01-01'  # tim0='2012-01-01'
    #
    fss = rss + xcod + '.csv'
    # -------------------
    xfg = os.path.exists(fss)
    xd0 = []
    xd = []
    if xfg:
        xd0 = pd.read_csv(fss, index_col=0, parse_dates=[0], encoding='gbk')
        # print(xd0.head())
        xd0 = xd0.sort_index(ascending=False)
        # tim0=xd0.index[0]
        _xt = xd0.index[0]  # xt=xd0.index[-1]###
        s2 = str(_xt)
        tim0 = s2.split(" ")[0]

    print('\n', xfg, fss, ",", tim0)
    # -----------
    try:
        xd = ts.get_h_data(xcod, start=tim0, end=None, retry_count=5, pause=1)  # Day9
        # xd=ts.get_hist_data(xcod,start=tim0,end=None,retry_count=5,pause=1,ktype=xtyp)
        # -------------
        if xd is not None:
            if (len(xd0) > 0):
                xd2 = xd0.append(xd)
                #  flt.dup 
                xd2["index"] = xd2.index
                xd2.drop_duplicates(subset='index', keep='last', inplace=True)
                del (xd2["index"])
                # xd2.index=pd.to_datetime(xd2.index)
                xd = xd2

            xd = xd.sort_index(ascending=False)
            xd = np.round(xd, 3)
            xd.to_csv(fss, encoding='gbk')
    except IOError:
        pass  # skip,error

    return xd


def down_stk_all(qx, finx):
    '''
    根据finx股票列表文件，下载所有，或追加日线数据
    自动去重，排序
    
    '''
    dinx = pd.read_csv(finx, encoding='gbk')
    print(finx)
    xn9 = len(dinx['code'])
    for i, xc in enumerate(dinx['code']):
        code = "%06d" % xc
        print("\n", i, "/", xn9, "code,", code)
        # ---
        qx.code = code
        down_stk_cn010(qx)


def down_stk_inx(qx, finx):
    dinx = pd.read_csv(finx, encoding='gbk')
    print(finx)

    xn9 = len(dinx['code'])
    for i in range(xn9):
        # for xc,xtim0 in dinx['code'],dinx['tim0']:
        d5 = dinx.iloc[i]
        xc = d5['code']
        xtim0 = d5['tim0']
        i += 1
        code = "%06d" % xc
        print("\n", i, "/", xn9, "code,", code, xtim0)
        # ---
        qx.code = code
        down_stk_cn020inx(qx, xtim0)

'''

def down_stk_yahoo010(qx, ftg):
   
		美股数据下载子程序
		Args:
        qx (zwDatX): 
        ftg,数据文件名
        
    :ivar xcod (int): 股票代码
    :ivar xdat (pd.DataFrame): yahoo xcod股票数据
   
    try:
        xcod = qx.code
        xdat = web.DataReader(xcod, "yahoo", start="1/1/1900")
        xdat.to_csv(ftg)
        print(ftg)
    except IOError:
        pass  # skip,error

'''

# --------stk.InxLib.xxx

def stkInxLibRd(qx):
    '''
		读取指定的大盘数据到zw.stkInxLib
		
		Args:
            
    :
    qx.stkInxRDat='\\zwdat\\cn\\xday\\''    #大盘指数数据源路径
    qx.stkInxCode='000001'    #大盘指数代码
    qx.stkInxName='sz001'    #大盘指数名称，拼音
    qx.stkInxCName='上证指数'    #大盘指数中文名称，拼音
    #
    zw.stkInxLib=None  #全局变量，大盘指数，内存股票数据库
    
    '''
    if qx.stkInxCode != '':
        fss = qx.stkInxRDat + qx.stkInxCode + ".csv"
        xfg = os.path.exists(fss)
        if xfg:
            df10 = pd.read_csv(fss, index_col=0, parse_dates=[0])
            df10 = df2zwAdj(df10)
            zw.stkInxLib = df10.sort_index()


def stkInxLibSet8XTim(qx, dtim0, dtim9):
    ''' 根据时间段，切割大盘指数数据 zw.stkInxLib
    
    Args:
        dtim0（str）：起始时间
        dtim9（str）:结束时间
            
    :ivar
    zw.stkInxLib，大盘指数数据
    '''
    df10 = zw.stkInxLib
    # print(df10.head())
    if dtim0 == '':
        df20 = df10
    else:
        df20 = df10[(df10.index >= dtim0) & (df10.index <= dtim9)]
        # df20=df10[(df10['date']>=dtim0)&(df10['date']<=dtim9)]

    zw.stkInxLib = df20.sort_index()


# --------stk.Lib.xxx



def stkLibRd(xlst, rdir):
    '''
		读取指定的股票数据到stkLib，可多只股票，以及股票代码文件名
		
		Args:
        xlst (list): 指定股票代码列表,
          如果xlst参数首字母是'@'，表示是股票代码文件名，而不是代码本身
          用于批量导入股票代码 
        rdir (str)：数据类存放目录 
            
    :ivar xcod (int): 股票代码
    
    '''
    zw.stkLib = {}  # 全局变量，相关股票的交易数据
    zw.stkLibCode = []  # 全局变量，相关股票的交易代码

    #
    x0 = xlst[0]
    if x0.find('@') == 0:
        fss = x0[1:]  # print('fss',fss)  #fss=_rdatInx+fs0
        flst = pd.read_csv(fss, dtype=str, encoding='gbk')
        xlst = list(flst['code'])
        # print(xlst)
    for xcod in xlst:
        fss = rdir + xcod + ".csv"
        xfg = os.path.exists(fss)
        if xfg:
            try:
                df10 = pd.read_csv(fss, index_col=0, parse_dates=[0])
                df10 = df2zwAdj(df10)
            except:
                print('读取文件失败：', fss)
            zw.stkLib[xcod] = df10.sort_index()
            zw.stkLibCode.append(xcod)


def stkLibPr():
    ''' 输出股票数据 
            
    :ivar xcod (int): 股票代码
    '''

    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        print('\n::code,', xcod)
        print(df10.head())
    print('\n stk code num', len(zw.stkLibCode))


def stkLibSet8XTim(dtim0, dtim9):
    ''' 根据时间段，切割股票数据
    
    Args:
        dtim0（str）：起始时间
        dtim9（str）:结束时间
            
    :ivar xcod (int): 股票代码
    '''
    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        if dtim0 == '':
            df20 = df10
        else:
            df20 = df10[(df10.index >= dtim0) & (df10.index <= dtim9)]
        #
        # zw.stkLibCode.append(xcod)
        zw.stkLib[xcod] = df20.sort_index()
        # print(zw.stkLib[xcod])
        # print(df20)


def stkLibSetDVix():
    ''' 根据时间段，切割股票数据
    
    Args:
        dtim0（str）：起始时间
        dtim9（str）:结束时间
            
    :ivar xcod (int): 股票代码
    '''
    for xcod in zw.stkLibCode:
        df10 = zw.stkLib[xcod]
        df10['dvix'] = df10['dprice'] / df10['dprice'].shift(1) * 100
        #
        zw.stkLib[xcod] = np.round(df10, 2)


# --------stk.Lib.get.xxx
def stkGetVars(qx, ksgn):
    '''
      获取股票代码，指定字段的数据
    
    Args:
        qx (zwQuantX): zwQuantX交易数据包
        ksgn (str): qx.stkCode,qx.xtim,qx.stkSgnPrice 
        '''
    d10 = zw.stkLib[qx.stkCode]
    d01 = d10[qx.xtim:qx.xtim]
    #
    dval = 0
    if len(d01) > 0:
        d02 = d01[ksgn]
        dval = d02[0]

    return dval


def stkGetPrice(qx, ksgn):
    '''
      获取当前价格
    
    Args:
        qx (zwQuantX): zwQuantX交易数据包
        ksgn (str): 价格模式代码
        '''
    d10 = zw.stkLib[qx.stkCode]
    d01 = d10[qx.xtim:qx.xtim]
    #
    price = 0
    if len(d01) > 0:
        d02 = d01[ksgn]
        price = d02[0]
        if pd.isnull(price):
            d02 = d01['dprice']
            price = d02[0]

    return price


def stkGetPrice9x(qx, ksgn):
    '''
      获取首个、末个交易日数据
    
    Args:
        qx (zwQuantX): zwQuantX交易数据包
        ksgn (str): 价格模式代码
        '''
    d10 = zw.stkLib[qx.stkCode]
    # d05=d10[qx.stkSgnPrice]
    d05 = d10[ksgn]
    price0 = d05[0]
    price9 = d05[-1]

    return price0, price9


def stkLibGetTimX(xcod):
    '''
    返回指定股票代码首个、末个交易日时间数据
    
    Args:
        xcod (int): 股票代码
        '''
    d10 = zw.stkLib[xcod]
    d01 = d10.index
    xtim0 = d01[0]
    xtim9 = d01[-1]
    # xtim0s=xtim0.strftime()

    return xtim0, xtim9


def stkLibName8Code(xcod):
    ''' 根据股票代码，返回股票中文、英文/拼音缩写名称
    
    Args:
        xcod (int): 股票代码
        '''
    d10 = zw.stkCodeTbl[zw.stkCodeTbl['code'] == xcod]
    # print(d10)
    enam = ''
    cnam = ''
    if len(d10) > 0:
        xc = d10.index[0]
        enam = d10.at[xc, 'ename']
        cnam = d10.at[xc, 'cname']
        # print('c',xc,cnam,enam)

    return enam, cnam


# --------stk.xxx
def stkValCalc(qx, xdicts):
    ''' 计算 xdicts 内所有的股票总价值
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        xdicts (list)：所选股票代码列表 
            
    :ivar xcod (int): 股票代码
    '''
    dsum9 = 0
    for xcod, xnum in xdicts.items():
        qx.stkCode = xcod
        # price=stkGetPrice(qx,'dprice')
        price = stkGetPrice(qx, qx.priceCalc)
        dsum = price * xnum
        dsum9 = dsum9 + dsum
        # print('@c',qx.xtim,price,dsum,dsum9)

    return dsum9


# --------xbars.xxx
def xbarPr(bars):
    ''' 输出数据包数据
    '''
    for xd in bars:
        xd.prXBar()
        print('')


def xbarGet8Tim(xcod, xtim):
    ''' 根据指定股票代码。时间，获取数据包
    
    Args:
        xcod (int): 股票代码
        xtim (str): 交易时间
        '''

    d10 = zw.stkLib[xcod]
    d02 = d10[xtim:xtim]

    return d02


def xbarGet8TimExt(xcod, xtim):
    '''  根据指定股票代码。时间，获取数据包及股票数据
    
    Args:
        xcod (int): 股票代码
        xtim (str): 交易时间
        '''

    d10 = zw.stkLib[xcod]
    d02 = d10[xtim:xtim]

    return d02, d10


# --------xtrd.xxx

def xtrdObjSet(qx):
    ''' 设置交易节点数据
    
    Args:
        qx (zwDatX): zwQuant数据包   
    #xtrdName=['date','ID','mode','code','dprice','num','kprice','sum','cash']
        '''
    b2 = pd.Series(zw.xtrdNil, index=zw.xtrdName)
    b2['date'] = qx.xtim
    b2['code'] = qx.stkCode
    b2['num'] = qx.stkNum
    if qx.stkNum != 0:
        b2['mode'] = zwt.iff3(qx.stkNum, 0, 'sell', '', 'buy')
        b2['dprice'] = stkGetVars(qx, qx.priceWrk)
        # kprice=stkGetVars(qx,qx.priceBuy)
        kprice = stkGetPrice(qx, qx.priceBuy)
        b2['kprice'] = kprice
        b2['sum'] = kprice * qx.stkNum
        dcash9 = qx.qxUsr['cash']
        b2['cash'] = dcash9 - kprice * b2['num']

    # print('\nb2\n',b2)
    return b2


def xtrdChkFlag(qx):
    ''' 检查是不是有效交易
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        #qx.stkNum，>0，买入股票；<0，卖出股票；-1；卖出全部股票
        #预设参数：qx.qxUsr 
    
    Return：
        xfg,True,有效交易；False，无效交易
        b2：有效交易的数据包 Bar
        
    :ivar xnum (int): 用户持有资产总数
    '''

    kfg = False
    b2 = None
    qx.trdNilFlag = False
    dcash9 = qx.qxUsr['cash']
    dnum = qx.stkNum
    dnum5 = abs(dnum)
    numFg = zwt.xinEQ(dnum5, qx.stkNum0, qx.stkNum9)
    # --------
    # b2=xtrdObjSet(qx) #print('::b2\n',b2)
    if dnum > 0:
        # dsum=b2['sum']
        kprice = stkGetVars(qx, qx.priceBuy)
        dsum = kprice * dnum
        # 股票买入股票总数，必须在限额内：100-2w手，总值不能超过现金数，买空需修改此处
        if numFg:
            if dsum < dcash9:
                kfg = True
            else:
                qx.trdNilFlag = True
    else:
        if qx.stkCode in qx.qxUsrStk:
            # print('@',qx.stkCode,dnum)
            xnum = qx.qxUsrStk[qx.stkCode]
            if dnum == -1:
                qx.stkNum = -xnum
                kfg = True
            else:
                kfg = zwt.iff2(dnum5 <= xnum, True, False)
            #
            qx.trdNilFlag = not kfg
        elif dnum != -1:
            qx.trdNilFlag = True

            #
    if kfg or qx.trdNilFlag:
        b2 = xtrdObjSet(qx)  # 设置交易节点
    else:
        qx.stkNum = 0

    return kfg, b2


def xtrdChkFlag00(qx):
    ''' 检查是不是有效交易
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        #qx.stkNum，>0，买入股票；<0，卖出股票；-1；卖出全部股票
        #预设参数：qx.qxUsr 
    
    Return：
        xfg,True,有效交易；False，无效交易
        b2：有效交易的数据包 Bar
        
    :ivar xnum (int): 用户持有资产总数
    '''

    kfg = False
    b2 = None
    dcash9 = qx.qxUsr['cash']
    # --------
    # b2=xtrdObjSet(qx) #print('::b2\n',b2)
    if qx.stkNum > 0:
        # dsum=b2['sum']
        kprice = stkGetVars(qx, qx.priceBuy)
        dsum = kprice * qx.stkNum
        # 股票买入股票总数，必须在限额内：100-2w手，总值不能超过现金数，买空需修改此处
        kfg = (zwt.xinEQ(qx.stkNum, qx.stkNum0, qx.stkNum9) and (dsum < dcash9))
    else:
        if qx.stkCode in qx.qxUsrStk:
            xnum = qx.qxUsrStk[qx.stkCode]
            if (qx.stkNum == -1) or (abs(qx.stkNum) >= xnum):
                qx.stkNum = -xnum
                kfg = True
            elif abs(qx.stkNum) < xnum:
                kfg = True

    #
    if kfg:
        b2 = xtrdObjSet(qx)  # 设置交易节点
    else:
        qx.stkNum = 0

    return kfg, b2


def xusrStkNum(qx, xcod):
    ''' 返回用户持有的 xcod 股票数目
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        xcod (int): 股票代码
        '''

    dnum = 0
    if xcod in qx.qxUsrStk:
        dnum = qx.qxUsrStk[xcod]
    return dnum


def xusrUpdate(qx):
    ''' 更新用户数据
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        
        '''

    qx.qxUsr['date'] = qx.xtim
    # dcash=qx.qxUsr['cash']
    # qx.qxUsr['cash']=dcash-b2['sum']
    stkVal = stkValCalc(qx, qx.qxUsrStk)
    qx.qxUsr['stkVal'] = stkVal
    dval0 = qx.qxUsr['val']
    dval = qx.qxUsr['cash'] + stkVal
    qx.qxUsr['val'] = dval
    # qx.qxUsr['dret'] = (qx.qxUsr['val'] - dval0) / dval0
    # # print('\n::xbarUsr\n',qx.qxUsrStk)
    # # print('stkVal',stkVal)
    #
    # # ---------drawdown.xxx
    # if dval > qx.downHigh:
    #     qx.downHigh = dval
    #     qx.downLow = dval
    #     # qx.downHighTime=date.today()
    #     qx.downHighTime = qx.xtim
    #     # qx.downHighTime=datetime.dateTime
    # else:
    #     qx.downLow = min(dval, qx.downLow)
    # # ----------
    # qx.qxUsr['downHigh'] = qx.downHigh
    # qx.qxUsr['downLow'] = qx.downLow
    # kmax = downKMax(qx.downLow, qx.downHigh)
    # qx.downKMax = min(qx.downKMax, kmax)
    # qx.qxUsr['downKMax'] = qx.downKMax
    # # xday=parse(qx.xtim)-parse(qx.downHighTime)
    # nday = rrule.rrule(rrule.DAILY, dtstart=parse(qx.downHighTime), until=parse(qx.xtim)).count()
    #
    # dmax = max(qx.downMaxDay, nday - 1)
    # qx.downMaxDay = dmax
    # qx.qxUsr['downDay'] = qx.downMaxDay


def xusr4xtrd(qx, b2):
    ''' 根据交易数据，更新用户数据 qxUsr
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        b2 (pd.Series): 有效交易的数据包 Bar
            
    :ivar xcod (int): 股票代码
    '''

    xcod = b2['code']
    if xcod != '':
        xfg = xcod in qx.qxUsrStk
        # s2=zwBox.xobj2str(b2,zw.xbarName) #print(xfg,'::b2,',s2)

        if xfg:
            xnum = qx.qxUsrStk[xcod]
            xnum2 = xnum + b2['num']
            qx.qxUsrStk[xcod] = xnum2
            if xnum2 == 0: del (qx.qxUsrStk[xcod])
        else:
            qx.qxUsrStk[xcod] = b2['num']

        qx.qxUsr['cash'] = qx.qxUsr['cash'] - b2['sum']


def xtrdLibAdd(qx):
    ''' 添加交易到 xtrdLib
    
    Args:
        qx (zwQuantX): zwQuantX数据包

    '''

    qx.qxIDSet()
    # print('qx.qxID',qx.qxID)
    qx.xtrdChk['ID'] = qx.qxID
    # xbarUsrUpdate(qx,qx.xtrdChk)
    xusr4xtrd(qx, qx.xtrdChk)  # qx.qxUsr['cash']=qx.qxUsr['cash']-b2['sum']
    qx.xtrdLib = qx.xtrdLib.append(qx.xtrdChk.T, ignore_index=True)


def xtrdLibNilAdd(qx):
    ''' 添加交易到空头记录 xtrdNilLib
    
    Args:
        qx (zwQuantX): zwQuantX数据包

    '''
    qx.xtrdChk['ID'] = 'nil'
    qx.xtrdNilLib = qx.xtrdNilLib.append(qx.xtrdChk.T, ignore_index=True)


# --zw.ret.xxx

def zwRetTradeCalc(qx, pyqt_mode=False):
    ''' 输出、计算交易数据
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        
        '''

    df = qx.xtrdLib
    xbar = qx.qxLib.iloc[-1]
    xtim9 = xbar['date']

    sum9 = -1 * df['sum'].sum()
    print('交易总次数：%d' % len(df))
    print('交易总盈利：%.2f' % sum9)
    qx.result_info.append(['交易总次数', '%d' % len(df)])
    # len(df)
    qx.result_info.append(['交易总盈利' , '%.2f' % sum9])

    # print('交易总支出：%.2f' %sumPut)
    # print('交易总收入：%.2f' %sumGet)
    # print('交易收益差：%.2f' %sumx)
    print('')
    # print('盈利交易数：%d' % numAdd)
    # print('盈利交易金额：%.2f' % sumAdd)
    # print('亏损交易数：%d' % numDec)
    # print('亏损交易金额：%.2f' % sumDec)
    # print('@t',qx.xtim)
    qx.xtim = xtim9


def zwRetPr(qx):
    ''' 输出、计算回报率
    
    Args:
        qx (zwQuantX): zwQuantX数据包

    '''
    # ---回报测试

    retAvg = qx.qxLib['dret'].mean()
    retStd = qx.qxLib['dret'].std()
    dsharp = sharpe_rate(qx.qxLib['dret'], qx.rfRate)
    dsharp0 = sharpe_rate(qx.qxLib['dret'], 0)
    dcash = qx.qxUsr['cash']
    dstk = stkValCalc(qx, qx.qxUsrStk)  # 因为个人添加了到期清仓的机制，所以dstk应该为0
    dval = dstk + dcash
    dret9 = (dval - qx.mbase) / qx.mbase

    print('')
    print("最终资产价值 Final portfolio value: $%.2f" % dval)
    print("最终现金资产价值 Final cash portfolio value: $%.2f" % dcash)
    print("最终证券资产价值 Final stock portfolio value: $%.2f" % dstk)
    print("累计回报率 Cumulative returns: %.2f %%" % (dret9 * 100))
    print("平均日收益率 Average daily return: %.3f %%" % (retAvg * 100))
    print("日收益率方差 Std. dev. daily return:%.4f " % (retStd))
    print('')
    print("夏普比率 Sharpe ratio: %.3f,（%.2f利率）" % (dsharp, qx.rfRate))
    print("无风险利率 Risk Free Rate: %.2f" % (qx.rfRate))
    print("夏普比率 Sharpe ratio: %.3f,（0利率）" % (dsharp0))
    print('')
    print("最大回撤率 Max. drawdown: %.4f %%" % (abs(qx.downKMax)))
    print("最长回撤时间 Longest drawdown duration:% d" % qx.downMaxDay)
    print("回撤时间(最高点位) Time High. drawdown: ", qx.downHighTime)
    print("回撤最高点位 High. drawdown: %.3f" % qx.downHigh)
    print("回撤最低点位 Low. drawdown: %.3f" % qx.downLow)
    print('')
    print("时间周期 Date lenght: %d (Day)" % qx.periodNDay)
    print("时间周期（交易日） Date lenght(weekday): %d (Day)" % qx.wrkNDay)

    print("开始时间 Date begin: %s" % qx.xtim0)
    print("结束时间 Date lenght: %s" % qx.xtim9)
    print('')
    print("项目名称 Project name: %s" % qx.prjName)
    print("策略名称 Strategy name: %s" % qx.staName)
    print("股票代码列表 Stock list: ", zw.stkLibCode)
    print("策略参数变量 staVars[]: ", qx.staVars)
    print('')

    if qx.pyqt_mode_flag == True:
        qx.result_info.append(['最终资产价值' , '$%.2f' % dval])
        qx.result_info.append(['最终现金资产价值' , '$%.2f' % dcash])
        qx.result_info.append(['最终证券资产价值' , '$%.2f' % dstk])
        qx.result_info.append(['累计回报率' , '%.2f' % (dret9 * 100)])
        qx.result_info.append(['平均日收益率' , '%.3f' % (retAvg * 100)])
        qx.result_info.append(['日收益率方差' , '%.4f' % retStd])
        qx.result_info.append(['夏普比率' , '%.3f,（%.2f利率）' % (dsharp, qx.rfRate)])
        qx.result_info.append(['无风险利率' , '%.2f' % qx.rfRate])
        qx.result_info.append(['夏普比率（无风险）' , '%.3f' % dsharp0])
        qx.result_info.append(['最大回撤率' , '%.4f' % abs(qx.downKMax)])
        qx.result_info.append(['最长回撤时间' , '%d' % qx.downMaxDay])
        qx.result_info.append(['回撤时间(最高点位)' , qx.downHighTime])
        qx.result_info.append(['回撤最高点位' , '%.3f' % qx.downHigh])
        qx.result_info.append(['回撤最低点位' , '%.3f' % qx.downLow])
        qx.result_info.append(['时间周期' , '%d (Day)' % qx.periodNDay])
        qx.result_info.append(['时间周期（交易日）' , '%d (Day)' % qx.wrkNDay])
        qx.result_info.append(['开始时间' , qx.xtim0])
        qx.result_info.append(['结束时间' , qx.xtim9])
        qx.result_info.append(['项目名称' , '%s' % qx.prjName])
        qx.result_info.append(['策略名称' , '%s' % qx.staName])
        # qx.result_info.append(['股票代码列表' , '  '.join(zw.stkLibCode)])
        qx.result_info.append(['策略参数变量 staVars[]' , '  '.join([str(i) for i in qx.staVars])])
        # qx.result_info.append(['最大回撤率' , '%.4f' % downKMax])


# -------------qx.xxxx
def qxObjSet(xtim, stkVal, dcash, dret):
    ''' 设置 xtrdLib 单次交易节点数据
    
    Args:
        xtim (str): 交易时间
        stkVal (int): 股票总价值
        dcash (int): 资金
        dret (float): 回报率

    '''
    qx10 = pd.Series(zw.qxLibNil, index=zw.qxLibName)
    qx10['date'] = xtim
    qx10['cash'] = dcash
    # stkVal=xbarStkSum(qx10['xBars'],xtim)
    # stkVal=0
    qx10['stkVal'] = stkVal
    qx10['val'] = stkVal + dcash

    return qx10


# -------------



def xedit_zwXDat(df):
    ''' 编辑用户数据格式
    
    Args:
        df (pd.DataFrame): 股票数据
            
            '''
    df = df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    df.sort_index(ascending=True, inplace=True)

    dx = df['open']
    df['xdiff'] = df['high'] - df['low']
    df['z-xdiff'] = df['xdiff'] * 1000 / dx
    df['z-xdiff'] = df['z-xdiff'].round(0)
    df['z-open'] = df['open'] * 1000 / dx.shift(1)
    df['z-open'] = df['z-open'].round(0)
    df['z-high'] = df['high'] * 1000 / dx
    df['z-high'] = df['z-high'].round(0)
    df['z-low'] = df['low'] * 1000 / dx
    df['z-low'] = df['z-low'].round(0)
    df['z-close'] = df['close'] * 1000 / dx
    df['z-close'] = df['z-close'].round(0)

    df['ma5'] = pd.rolling_mean(df['close'], window=5)
    df['ma10'] = pd.rolling_mean(df['close'], window=10)
    df['ma20'] = pd.rolling_mean(df['close'], window=20)
    df['ma30'] = pd.rolling_mean(df['close'], window=30)

    df['v-ma5'] = pd.rolling_mean(df['volume'], window=5)
    df['v-ma10'] = pd.rolling_mean(df['volume'], window=10)
    df['v-ma20'] = pd.rolling_mean(df['volume'], window=20)
    df['v-ma30'] = pd.rolling_mean(df['volume'], window=30)

    c20 = df.columns  # print(c20)
    if ('amount' in c20): del (df['amount'])
    if ('Adj Close' in c20): del (df['Adj Close'])

    df = df.round(decimals=2)

    clst = ["open", "high", "low", "close", "volume", "xdiff", "z-open", "z-high", "z-low", "z-close", "z-xdiff", "ma5",
            "ma10", "ma20", "ma30", "v-ma5", "v-ma10", "v-ma20", "v-ma30"]
    d30 = pd.DataFrame(df, columns=clst)

    return d30


# ------------
def df2yhaoo(df0):
    ''' 股票数据格式转换，转换为 Yahoo 格式
    
    Args:
        df0 (pd.DataFrame): 股票数据
        
    #Date,Open,High,Low,Close,Volume,Adj Close        
        '''

    clst = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'date': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
    # df0=df0.round(decimals=2)


    df2['Date'] = df0['Date']
    df2['Open'] = df0['Open']
    df2['High'] = df0['High']
    df2['Low'] = df0['Low']
    df2['Close'] = df0['Close']
    df2['Adj Close'] = df0['Close']
    df2['Volume'] = df0['Volume']
    df2 = df2.set_index(['Date'])

    return df2


def df2cnstk(df0):
    ''' 股票数据格式转换，转换为中国 A 股格式
    
    Args:
        df0 (pd.DataFrame): 股票数据
        
    #date,open,high,close,low,volume,amount    
        '''

    clst = ["open", "high", "low", "close", "volume", "amount"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    # df0=df0.round(decimals=2)

    df2['date'] = df0['date']
    df2['open'] = df0['open']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2['close'] = df0['close']
    df2['volume'] = df0['volume']

    df2 = df2.set_index(['date'])

    return df2


def df2zw(df0):
    ''' 股票数据格式转换，转换为 zw 格式
    
    Args:
        df0 (pd.DataFrame): 股票数据

    '''

    clst = ["open", "high", "low", "close", "volume"]
    df2 = pd.DataFrame(columns=clst)
    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    # df0=df0.round(decimals=2)

    df2['date'] = df0['date']
    df2['open'] = df0['open']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2['close'] = df0['close']
    df2['volume'] = df0['volume']

    df2 = df2.set_index(['date'])

    return df2


def df2zwAdj(df0):
    ''' 股票数据格式转换，转换为 zw 增强版格式，带 adj close

    Args:
        df0 (pd.DataFrame): 股票数据
        '''

    df0 = df0.rename(
        columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
                 "Adj Close": "adj close"})
    ksgn = 'adj close'
    if ksgn not in df0.columns:
        df0[ksgn] = df0['close']
    return df0


# def df2zwAdj(df0):
#     ''' 股票数据格式转换，转换为 zw 增强版格式，带 adj close
#
#     Args:
#         df0 (pd.DataFrame): 股票数据
#         '''
#
#     clst = ["open", "high", "low", "close", "volume", "adj close"]
#     df2 = pd.DataFrame(columns=clst)
#     df0 = df0.rename(
#         columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
#                  "Adj Close": "adj close"})
#     # df0=df0.round(decimals=2)
#
#     df0['date'] = df0.index
#     df2['date'] = df0['date']
#     for col_name in clst:
#         if col_name in df0.columns:
#             df2[col_name] = df0[col_name]
#
#     # df2['open'] = df0['open']
#     # df2['high'] = df0['high']
#     # df2['low'] = df0['low']
#     # df2['close'] = df0['close']
#     # df2['volume'] = df0['volume']
#     # 'adj close'
#     ksgn = 'adj close'
#     if ksgn in df0.columns:
#         df2[ksgn] = df0[ksgn]
#     else:
#         df2[ksgn] = df0['close']
#
#     # ----index
#     df2 = df2.set_index(['date'])
#
#     return df2


# -----OHLC
def stk_col_renLow(dat):
    ''' 股票数据格式转换，转换小写列名称
    
    Args:
        dat (pd.DataFrame): 股票数据
        '''

    dat = dat.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
                              "Adj Close": "adj close"})

    return dat


def stk_copy_OHLC(dat0):
    ''' 复制股票 OHLC 数据
    
    Args:
        dat0 (pd.DataFrame): 股票数据
        '''

    df0 = dat0
    df0 = stk_col_renLow(df0)
    df2 = pd.DataFrame(columns=['open', 'close', 'high', 'low'])
    df2['open'] = df0['open']
    df2['close'] = df0['close']
    df2['high'] = df0['high']
    df2['low'] = df0['low']
    df2.index = df0.index

    return df2


# ---------------- qt.misc.xxx
def downKMax(dlow, dhigh):
    '''
    downKMax(dlow,dhigh):
        回缩率计算函数
        低位，高位，指的是投资组合的市场总值
    【输入】：
    dlow，当前的低位，低水位，也称，lowerWatermark
    dhigh，当前的高位，高水位，也称，highWatermark
    【输出】
    回缩率,百分比数值
    '''

    if dhigh > 0:
        kmax = (dlow - dhigh) / float(dhigh) * 100
    else:
        kmax = 0

    return kmax


def sharpe_rate(ser_return, rfRate, ntim=252, log_flag=False):
    '''
    sharpe_rate(ser_return,rfRate,ntim=252):
        计算夏普指数
    【输入】
    	ser_return (Series): 收益率Series（根据ntim，按日、小时、保存）
      rfRate (float): 无风险收益率
      ntim (int): 每年交易次数（按天、小时、等计数）
         采用小时(60分钟)线数据，ntim= 252* 6.5 = 1638.
    【输出】
        夏普指数数值
        '''

    '''如果不是对数收益率，则转化成对数收益率'''
    if log_flag == False:
        ser_return = np.log(ser_return + 1)
    ser_return.dropna(inplace=True)
    rstd = ser_return.std()
    '''如果波动率为0，说明ser_return是一个单一值，没有夏普比'''
    if rstd != 0:
        rmean = ser_return.mean()
        avgExRet = rmean - rfRate / ntim
        dsharp = avgExRet / rstd
        rsharp = dsharp * np.sqrt(ntim)
    else:
        rsharp = None
    return rsharp


# ----------sta.misc



# ----


def sta_dataPre0xtim(qx, xnam0):
    ''' 策略参数设置子函数，根据预设时间，裁剪数据源stkLib
    
    Args:
        qx (zwQuantX): zwQuantX数据包 
        xnam0 (str)： 函数标签

    '''

    # 设置当前策略的变量参数
    qx.staName = xnam0
    qx.rfRate = 0.05  # 无风险年收益，一般为0.05(5%)，计算夏普指数等需要
    # qx.stkNum9=20000   #每手交易，默认最多20000股
    #
    # 按指定的时间周期，裁剪数据源
    xt0k = qx.staVars[-2]
    xt9k = qx.staVars[-1]
    if (xt0k != '') or (xt9k != ''):
        # xtim0=parse('9999-01-01')
        # xtim9=parse('1000-01-01')
        # xtim0=xtim0.strftime('%Y-%m-%d')
        # xtim9=xtim9.strftime('%Y-%m-%d')
        if xt0k != '':
            if qx.xtim0 < xt0k:
                qx.xtim0 = xt0k
        if xt9k != '':
            if qx.xtim9 > xt9k:
                qx.xtim9 = xt9k
        qx.qxTimSet(qx.xtim0, qx.xtim9)
        stkLibSet8XTim(qx.xtim0, qx.xtim9)  # print('zw.stkLibCode',zw.stkLibCode)

    # ---stkInx 读取大盘指数数据，并裁剪数据源
    # print('finx',qx.stkInxCode)
    if qx.stkInxCode != '':
        stkInxLibRd(qx)
        stkInxLibSet8XTim(qx, qx.xtim0, qx.xtim9)

    # ============
    # ---设置qxUsr用户变量，起始数据
    qx.qxUsr = qxObjSet(qx.xtim0, 0, qx.money, 0)


def cross_Mod(qx):
    ''' 均线交叉策略，判断均线向上、向下趋势
    
    Args:
        qx (zwQuantX): zwQuantX数据包
        ksma (str)：均线数据列名称
    Return:
        1:above
        0:=
        -1:below
        '''

    kma = 'ma_%d' % qx.staVars[0]
    xbar = qx.xbarWrk
    dma, ma2n = xbar[kma][0], xbar['ma2n'][0]
    dp, dp2n = xbar['dprice'][0], xbar['dp2n'][0]
    #
    kmod = -9
    if (dp > dma) and (dp2n < ma2n) and (dp > dp2n):
        kmod = 1
        # print('   crs',kmod,'xbar\n',xbar)
    elif (dp < dma) and (dp2n > ma2n) and (dp < dp2n):
        kmod = -1
        # print('   crs',kmod,'xbar\n',xbar)

    return kmod
