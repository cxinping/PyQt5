# -*- coding: utf-8 -*- 
'''
    模块名：zwpd_talib.py
    默认缩写：zwta,示例：import zwpd_talib as zwta
    【简介】
    zw版的talib函数封装，第一批以pandas_talib.py的29个函数为蓝本。

    zw_talib函数库v0.5版，所有33个函数，均已测试通过，
    运行平台：python3.5，zwPython2016m2    
     
     zw量化，py量化第一品牌
     网站:http://www.ziwang.com zw网站
     py量化QQ总群  124134140   千人大群 zwPython量化&大数据 
     
     开发：zw量化开源团队 2016.03.28
     
    pandas_talib.py参见：
    https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code
    https://github.com/panpanpandas/ultrafinance/blob/master/ultrafinance/pyTaLib/pandasImpl.py
    默认数据格式，采用zwDat标准，全部小写
    ohlcv:open,high,low,close,volumns

---------zwtalib 首批函数名称
:: ACCDIST(df, n):集散指标(A/D)——Accumulation/Distribution,是由价格和成交量的变化而决定的
:: ADX(df, n, n_ADX): 	 #adx，中文全称：平均趋向指数，ADX指数是反映趋向变动的程度，而不是方向的本身;英文全称：Average Directional Index 或者Average Directional Movement Index
:: ATR(df, n): ATR,均幅指标（Average True Ranger）,取一定时间周期内的股价波动幅度的移动平均值，主要用于研判买卖时机
:: BBANDS(df, n):布林带.Bollinger Bands 
:: BBANDS_UpLow(df, n): zw改进版的布林带talib函数
:: CCI(df, n): CCI顺势指标(Commodity Channel Index),CCI指标，是由美国股市分析家唐纳德::蓝伯特（Donald Lambert）所创造的，是一种重点研判股价偏离度的股市分析工具。
:: COPP(df, n):估波指标（Coppock Curve）,又称“估波曲线”，通过计算月度价格的变化速率的加权平均值来测量市场的动量，属于长线指标。估波指标由Edwin::Sedgwick::Coppock于1962年提出，主要用于判断牛市的到来。该指标用于研判大盘指数较为可靠，一般较少用于个股；再有，该指标只能产生买进讯号。依估波指标买进股票后，应另外寻求其他指标来辅助卖出讯号。估波指标的周期参数一般设置为11、14，加权平均参数为10，也可以结合指标的平均线进行分析
:: Chaikin(df):佳庆指标（Chaikin Oscillator）,是由马可::蔡金（Marc Chaikin）提出的，聚散指标（A/D）的改良版本。
:: DONCH(df, n):奇安通道指标,Donchian Channel,该指标是由Richard Donchian发明的，是有3条不同颜色的曲线组成的，该指标用周期（一般都是20）内的最高价和最低价来显示市场的波动性;当其通道窄时表示市场波动较小，反之通道宽则表示市场波动比较大。
:: EMA(df, n):指数平均数指标(Exponential Moving Average，EXPMA或EMA),指数平均数指标也叫EXPMA指标，它也是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分析，用于判断价格未来走势的变动趋势。
:: EOM(df, n):简易波动指标(Ease of Movement Value)，又称EMV指标;它是由RichardW．ArmJr．根据等量图和压缩图的原理设计而成,目的是将价格与成交量的变化结合成一个波动指标来反映股价或指数的变动状况。由于股价的变化和成交量的变化都可以引发该指标数值的变动,因此,EMV实际上也是一个量价合成指标。
:: FORCE(df, n):劲道指数(Force Index);劲道指数是由亚历山大::埃尔德(Alexander Elder)博士设计的一种摆荡指标，藉以衡量每个涨势中的多头劲道与每个跌势中的空头劲道。劲道指数结合三项主要的市场资讯：价格变动的方向、它的幅度与成交量。它是由一个崭新而实用的角度，把成交量纳入交易决策中。
:: KELCH(df, n):肯特纳通道（Keltner Channel，KC）,肯特纳通道（KC）是一个移动平均通道，由叁条线组合而成(上通道、中通道及下通道)。通道，一般情况下是以上通道线及下通道线的分界作为买卖的最大可能性。若股价於边界出现不沉常的波动，即表示买卖机会。
:: KST(df, r1, r2, r3, r4, n1, n2, n3, n4): 确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
:: KST4(df, r1, r2, r3, r4, n1, n2, n3, n4): 	zw修订版，KST确然指标,确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
:: MA(df, n):移动平均线,Moving Average，即最常用的均线指标
:: MACD(df, n_fast, n_slow): #MACD指标信号和MACD的区别, MACD Signal and MACD difference，MACD是由一快及一慢指数移动平均（EMA）之间的差计算出来。“快”指短时期的EMA，而“慢”则指长时期的EMA，最常用的是12及26日EMA。
:: MFI(df, n): MFI,资金流量指标和比率,Money Flow Index and Ratio，资金流量指标又称为量相对强弱指标（Volume Relative Strength Index，VRSI）；根据成交量来计测市场供需关系和买卖力道。该指标是通过反映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度；来研判量能的趋势，预测市场供求关系和买卖力道，属于量能反趋向指标。	
:: MOM(df, n):动量线，英文全名MOmentum，简称MOM。“动量”这一名词，市场上的解释相当广泛。以Momentum命名的指标，种类更是繁多。综合而言，动量可以视为一段期间内，股价涨跌变动的比率。
:: MassI(df):梅斯线（Mass Index），梅斯线是Donald Dorsey累积股价波幅宽度之后，所设计的震荡曲线。本指标最主要的作用，在于寻找飙涨股或者极度弱势股的重要趋势反转点。MASS指标是所有区间震荡指标中，风险系数最小的一个。		
:: OBV(df, n):能量潮指标（On Balance Volume，OBV），OBV指标是葛兰维（Joe Granville）于本世纪60年代提出的，并被广泛使用。股市技术分析的四大要素：价、量、时、空。OBV指标就是从“量”这个要素作为突破口，来发现热门股票、分析股价运动趋势的一种技术指标。它是将股市的人气——成交量与股价的关系数字化、直观化，以股市的成交量变化来衡量股市的推动力，从而研判股价的走势。关于成交量方面的研究，OBV能量潮指标是一种相当重要的分析指标之一。
:: PPSR(df):支点，支撑线和阻力线.Pivot Points, Supports and Resistances；PIVOT指标的观念很简单，不需要计算任何东西，它纯粹只是一个分析反转点的方法而已。PIVOT意思是指“轴心”，轴心是用来确认反转的基准，所以PIVOT指标其实就是找轴心的方法；PIVOT指标，经常与布林带数据一起分析。
:: ROC(df, n):变动率(Rate of change,ROC)，ROC是由当天的股价与一定的天数之前的某一天股价比较，其变动速度的大小,来反映股票市场变动的快慢程度。ROC，也叫做变动速度指标、变动率指标或变化速率指标。	
:: RSI(df, n): RSI，相对强弱指标,Relative Strength Index，也称相对强弱指数、相对力度指数；RSI，是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。RSI通过特定时期内股价的变动情况计算市场买卖力量对比，来判断股票价格内部本质强弱、推测价格未来的变动方向的技术指标。
:: RSI100(df, n):zw版RSI相对强弱指数，取0..100之间的数值
:: STDDEV(df, n):标准偏差,Standard Deviation
:: STOD(df, n):随机指标D值,Stochastic oscillator %D；随机指标，又称KD指标，KDJ指标；随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。随机指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价，及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
:: STOK(df):随机指标K值,Stochastic oscillator %K 
:: TRIX(df, n):TRIX指标又叫三重指数平滑移动平均指标，Triple Exponentially Smoothed Average
:: TSI(df, r, s): TSI，真实强度指数,True Strength Index，TSI是相对强弱指数 (RSI) 的变体。TSI 使用价格动量的双重平滑指数移动平均线，剔除价格的震荡变化并发现趋势的变化。r一般取25，是一般取13。
:: ULTOSC(df): UOS，终极指标（Ultimate Oscillator），终极指标，由拉瑞::威廉（Larry Williams）所创。他认为现行使用的各种振荡指标，对于周期参数的选择相当敏感。不同的市况，不同参数设定的振荡指标，产生的结果截然不同。因此，选择最佳的参数组含，成为使用振荡指标之前，最重要的一道手续。为了将参数周期调和至最佳状况，拉瑞::威廉经过不断测试的结果，先找出三个周期不同的振荡指标，再将这些周期参数，按照反比例的方式，制作成常数因子。然后，依照加权的方式，将三个周期不同的振荡指标，分别乘以不同比例的常数，加以综合制作成UOS指标。经过一连串参数顺化的过程后，UOS指标比一般单一参数的振荡指标，更能够顺应各种不同的市况。
:: Vortex(df, n):螺旋指标,Vortex Indicator，参见http://www.vortexindicator.com/VFX_VORTEX.PDF


'''

import sys,os
import numpy as np
import pandas as pd



#----

def ACCDIST(df, n,ksgn='close'): 
    '''
    def ACCDIST(df, n,ksgn='close'): 
    #集散指标(A/D)——Accumulation/Distribution
        是由价格和成交量的变化而决定的
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ad_{n}，输出数据
    '''
    xnam='ad_{d}'.format(d=n)
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    M = ad.diff(n - 1)  
    N = ad.shift(n - 1)  
    ROC = M / N  
    AD = pd.Series(ROC, name = xnam)  #'Acc/Dist_ROC_' + str(n)
    df = df.join(AD)  
    return df


def ADX(df, n, n_ADX,ksgn='close'):
    '''
    def ADX(df, n, n_ADX):
    adx，中文全称：平均趋向指数，ADX指数是反映趋向变动的程度，而不是方向的本身
    英文全称：Average Directional Index 或者Average Directional Movement Index
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        n_ADX,adx周期
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：adx_{n}_{n2}，输出数据
    '''
    i = 0
    UpI = []
    DoI = []
    xnam='adx_{n}_{n2}'.format(n=n,n2=n_ADX)
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        #..UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        UpMove = df['high'].iloc[i+1] - df['high'].iloc[i]
        DoMove = df['low'].iloc[i] - df['low'].iloc[i+1]
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        TR = max(df['high'].iloc[i+1], df[ksgn].iloc[i]) - min(df['low'].iloc[i+1], df[ksgn].iloc[i])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    ATR = pd.Series(pd.ewma(TR_s, span=n, min_periods=n))
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1) / ATR)
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1) / ATR)
    ds = pd.Series(pd.ewma(abs(PosDI - NegDI) / (PosDI + NegDI), span=n_ADX, min_periods=n_ADX - 1), name=xnam)
    ds.index=df.index;df[xnam]=ds
    #df = df.join(ds)  
    return df


def ATR(df, n,ksgn='close'):  
    '''
    def ATR(df, n,ksgn='close'):  
    #ATR,均幅指标（Average True Ranger）,取一定时间周期内的股价波动幅度的移动平均值，主要用于研判买卖时机
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：atr_{n}，输出数据
    '''    
    xnam='atr_{n}'.format(n=n)
    i = 0
    TR_l = [0]
    while i < len(df) - 1:  # df.index[-1]:
    # for i, idx in enumerate(df.index)
        # TR=max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR = max(df['high'].iloc[i + 1], df[ksgn].iloc[i] - min(df['low'].iloc[i + 1], df[ksgn].iloc[i]))
        TR_l.append(TR)
        i = i + 1;#print('#',i,TR)
    TR_s = pd.Series(TR_l)
    ds = pd.Series(pd.ewma(TR_s, span=n, min_periods=n), name=xnam)
    #df = df.join(ds)  
    ds.index=df.index;df[xnam]=ds
    #print('ds',ds.head())
    return df
    


def BBANDS(df, n,ksgn='close'):  
    '''
    def BBANDS(df, n,ksgn='close'):  
    布林带.Bollinger Bands  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：_{n}，_{n}b，输出数据
    '''    
    xnam='boll_{n}'.format(n=n)
    MA = pd.Series(pd.rolling_mean(df[ksgn], n))  
    MSD = pd.Series(pd.rolling_std(df[ksgn], n))  
    b1 = 4 * MSD / MA  
    B1 = pd.Series(b1, name = xnam+'b')  
    df = df.join(B1)  
    b2 = (df[ksgn] - MA + 2 * MSD) / (4 * MSD)  
    B2 = pd.Series(b2, name = xnam)  
    df = df.join(B2)  
    return df    


def BBANDS_UpLow(df, n,ksgn='close'):  
    '''
    BBANDS_UpLow(df, n,ksgn='close'):  
    zw改进版的布林带talib函数.Bollinger Bands  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了4栏：
            boll_ma，布林带均线数据
            boll_std，布林带方差据
            boll_up，布林带上轨带差据
            boll_low，布林带下轨带差据
    '''        
    df['boll_ma']=pd.Series(pd.rolling_mean(df[ksgn], n))  
    df['boll_std']= pd.Series(pd.rolling_std(df[ksgn], n))  
    #df[#MSD = pd.Series(pd.rolling_std(df[ksgn], n))  
    MA=df['boll_ma']
    MSD=df['boll_std']
    #
    knum=2
    df['boll_up']= MA + MSD * knum    #knum=numStdDev
    df['boll_low']= MA - MSD * knum

    return df 


def CCI(df, n,ksgn='close'):  
    '''
    def CCI(df, n,ksgn='close'):  
    CCI顺势指标(Commodity Channel Index)
    CCI指标，是由美国股市分析家唐纳德·蓝伯特（Donald Lambert）所创造的，是一种重点研判股价偏离度的股市分析工具。

    
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：cci_{n}，输出数据
    '''
    xnam='cci_{d}'.format(d=n)
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    CCI = pd.Series((PP - pd.rolling_mean(PP, n)) / pd.rolling_std(PP, n), name = xnam)  
    df = df.join(CCI)  
    
    return df
    

#Coppock Curve  
def COPP(df, n,ksgn='close'):  
    '''
    def COPP(df, n):  				
　　估波指标（Coppock Curve）又称“估波曲线”，通过计算月度价格的变化速率的加权平均值来测量市场的动量，属于长线指标。
　　估波指标由Edwin·Sedgwick·Coppock于1962年提出，主要用于判断牛市的到来。
    该指标用于研判大盘指数较为可靠，一般较少用于个股；再有，该指标只能产生买进讯号。
    依估波指标买进股票后，应另外寻求其他指标来辅助卖出讯号。
    估波指标的周期参数一般设置为11、14，加权平均参数为10，也可以结合指标的平均线进行分析

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：copp_{n}，输出数据
    '''
    xnam='copp_{d}'.format(d=n)
    M = df[ksgn].diff(int(n * 11 / 10) - 1)  
    N = df[ksgn].shift(int(n * 11 / 10) - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(int(n * 14 / 10) - 1)  
    N = df[ksgn].shift(int(n * 14 / 10) - 1)  
    ROC2 = M / N  
    Copp = pd.Series(pd.ewma(ROC1 + ROC2, span = n, min_periods = n), name = xnam)  
    df = df.join(Copp)  
    return df
    
#Chaikin Oscillator  
def CHAIKIN(df,ksgn='close'):   
    '''
    def CHAIKIN(df):					
    #佳庆指标（Chaikin Oscillator）
　　佳庆指标（CHAIKIN）是由马可·蔡金（Marc Chaikin）提出的，聚散指标（A/D）的改良版本。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：_{n}，输出数据
    '''
    xnam='ck'
    ad = (2 * df[ksgn] - df['high'] - df['low']) / (df['high'] - df['low']) * df['volume']  
    Chaikin = pd.Series(pd.ewma(ad, span = 3, min_periods = 2) - pd.ewma(ad, span = 10, min_periods = 9), name = xnam)  
    df = df.join(Chaikin)  
    return df
    

#Donchian Channel  
def DONCH(df, n):  
    '''
    def DONCH(df, n):      
      #奇安通道指标,Donchian Channel  
	该指标是由Richard Donchian发明的，是有3条不同颜色的曲线组成的，该指标用周期（一般都是20）内的最高价和最低价来显示市场的波动性
	当其通道窄时表示市场波动较小，反之通道宽则表示市场波动比较大。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：donch__{n}sr，中间输出数据
            donch__{n}，输出数据
    '''
    xnam='donch_{d}'.format(d=n)
    i = 0  
    DC_l = []  
    while i < n - 1:  
        DC_l.append(0)  
        i = i + 1  
    i = 0  
    while (i + n - 1) <=(len(df) - 1):  #df.index[-1]:  
        #DC = max(df['high'].ix[i:i + n - 1]) - min(df['low'].ix[i:i + n - 1])  
        DC = max(df['high'].iloc[i:i + n - 1]) - min(df['low'].iloc[i:i + n - 1])  
        DC_l.append(DC)  
        i = i + 1  
    #
    #DC_l.append(DC)  
    #
    DonCh = pd.Series(DC_l, name = xnam)   #'Donchian_' + str(n)
    
    #df = df.join(DonCh)  
    DonCh.index=df.index;
    df[xnam+'_sr']=DonCh
    df[xnam]=df[xnam+'_sr'].shift(n - 1)  
    #DonCh = DonCh.shift(n - 1)  
    return df
    


def EMA(df, n,ksgn='close'):  
    '''
    EMA(df, n,ksgn='close'):  
    #Exponential Moving Average  
    EMA是指数平滑移动平均线，也叫EXPMA指标，也称为：SMMA 
    是平均线的一个变种，EMA均线较MA更加专业一些。
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ema_{n}，输出数据
    '''
    xnam='ema_{n}'.format(n=n)
    EMA = pd.Series(pd.ewma(df[ksgn], span = n, min_periods = n - 1), name = xnam)  
    df = df.join(EMA)  
    return df    
   
    

#Ease of Movement  
def EOM(df, n):   
    '''
    def EOM(df, n):  					
    简易波动指标(Ease of Movement Value)，又称EMV指标
   它是由RichardW．ArmJr．根据等量图和压缩图的原理设计而成,目的是将价格与成交量的变化结合成一个波动指标来反映股价或指数的变动状况。
   由于股价的变化和成交量的变化都可以引发该指标数值的变动,因此,EMV实际上也是一个量价合成指标。


    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：eom_{n}，输出数据
            eom_x，10e10倍的输出数据
    '''
    xnam='eom_{d}'.format(d=n)
    EoM = (df['high'].diff(1) + df['low'].diff(1)) * (df['high'] - df['low']) / (2 * df['volume'])  
    Eom_ma = pd.Series(pd.rolling_mean(EoM, n), name = xnam)  
    df = df.join(Eom_ma)  
    df['eom_x']=df[xnam]*10e10
    return df



def FORCE(df, n,ksgn='close'):   
    '''
    def FORCE(df, n):					
    #劲道指数(Force Index)
　　劲道指数是由亚历山大·埃尔德(Alexander Elder)博士设计的一种摆荡指标，藉以衡量每个涨势中的多头劲道与每个跌势中的空头劲道。
　　劲道指数结合三项主要的市场资讯：价格变动的方向、它的幅度与成交量。它是由一个崭新而实用的角度，把成交量纳入交易决策中。

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：force__{n}，输出数据
          force_x，缩小10e7倍的输出数据
    '''
    xnam='force_{d}'.format(d=n)
    F = pd.Series(df[ksgn].diff(n) * df['volume'].diff(n), name = xnam)  
    df = df.join(F)  
    df['force_x']=df[xnam]/10e7
    return df

def KELCH(df, n,ksgn='close'):
    '''
    def KELCH(df, n):  				#肯特纳通道（Keltner Channel，KC）
　　肯特纳通道（KC）是一个移动平均通道，由叁条线组合而成(上通道、中通道及下通道)。
	KC通道，一般情况下是以上通道线及下通道线的分界作为买卖的最大可能性。
  	若股价於边界出现不沉常的波动，即表示买卖机会。    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了3栏：kc_m，中间数据
            kc_u，up上轨道数据
            kc_d，down下轨道数据
    '''
    xnam='kc_m'
    xnam2='kc_u'
    xnam3='kc_d'
    KelChM = pd.Series(pd.rolling_mean((df['high'] + df['low'] + df[ksgn]) / 3, n), name = xnam)  #'KelChM_' + str(n)
    KelChU = pd.Series(pd.rolling_mean((4 * df['high'] - 2 * df['low'] + df[ksgn]) / 3, n), name = xnam2)   #'KelChU_' + str(n)
    KelChD = pd.Series(pd.rolling_mean((-2 * df['high'] + 4 * df['low'] + df[ksgn]) / 3, n), name =xnam3)    #'KelChD_' + str(n)
    df = df.join(KelChM)  
    df = df.join(KelChU)  
    df = df.join(KelChD)  
    
    return df




def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    '''
    def KST(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    #KST Oscillator  
    确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。
    该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
    
    tst:
       (r1, r2, r3, r4, n1, n2, n3, n4) = (1, 2, 3, 4, 6, 7, 9, 9)
    '''
    '''
    
    【输入】
        df, pd.dataframe格式数据源
        r1..r4,n1..n4，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ksf，输出数据
    '''
    xnam='kst';
    M = df[ksgn].diff(r1 - 1)  
    N = df[ksgn].shift(r1 - 1)  
    ROC1 = M / N  
    M = df[ksgn].diff(r2 - 1)  
    N = df[ksgn].shift(r2 - 1)  
    ROC2 = M / N  
    M = df[ksgn].diff(r3 - 1)  
    N = df[ksgn].shift(r3 - 1)  
    ROC3 = M / N  
    M = df[ksgn].diff(r4 - 1)  
    N = df[ksgn].shift(r4 - 1)  
    ROC4 = M / N  
    #'KST_' + str(r1) + '_' + str(r2) + '_' + str(r3) + '_' + str(r4) + '_' + str(n1) + '_' + str(n2) + '_' + str(n3) + '_' + str(n4)
    KST = pd.Series(pd.rolling_sum(ROC1, n1) + pd.rolling_sum(ROC2, n2) * 2 + pd.rolling_sum(ROC3, n3) * 3 + pd.rolling_sum(ROC4, n4) * 4, name = xnam)  
    df = df.join(KST)  
    return df

def KST4(df, r1, r2, r3, r4,ksgn='close'): 
    '''
    def KST4(df, r1, r2, r3, r4, n1, n2, n3, n4,ksgn='close'): 
    zw修订版，KST确然指标
    确然指标（KST）又称为完定指标，该指标参考长、中、短期的变速率ROC，以了解不同时间循环对市场的影响。
    该指标将数个周期的价格变动率函数作加权以及再平滑绘制长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
    
    tst:
       (r1, r2, r3, r4) = (9,13,18,24);(12,20,30,40)
    
    【输入】
        df, pd.dataframe格式数据源
        r1,r2,r3,r4，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ksf，输出数据
    
    '''
    df=KST(df,r1, r2, r3, r4,r1, r2, r3, r4,ksgn)
    
    return df

 
def MA(df, n,ksgn='close'):  
    '''
    def MA(df, n,ksgn='close'):  
    #Moving Average  
    MA是简单平均线，也就是平常说的均线
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：ma_{n}，均线数据
    '''
    xnam='ma_{n}'.format(n=n)
    #ds5 = pd.Series(pd.rolling_mean(df[ksgn], n), name =xnam)  
    ds2=pd.Series(df[ksgn], name =xnam);
    ds5 = ds2.rolling(center=False,window=n).mean() 
    #print(ds5.head()); print(df.head())
    df = df.join(ds5)  
    
    return df
   
   


#MACD, MACD Signal and MACD difference  
def MACD(df, n_fast, n_slow,ksgn='close'): 
    '''
    def MACD(df, n_fast, n_slow):           
      #MACD指标信号和MACD的区别, MACD Signal and MACD difference   
	MACD是查拉尔·阿佩尔(Geral Appel)于1979年提出的，由一快及一慢指数移动平均（EMA）之间的差计算出来。
	“快”指短时期的EMA，而“慢”则指长时期的EMA，最常用的是12及26日EMA：

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了3栏：macd,sign,mdiff
    '''
    xnam='macd'.format(n=n_fast,n2=n_slow)
    xnam2='msign'.format(n=n_fast,n2=n_slow)
    xnam3='mdiff'.format(n=n_fast,n2=n_slow)
    EMAfast = pd.Series(pd.ewma(df[ksgn], span = n_fast, min_periods = n_slow - 1))  
    EMAslow = pd.Series(pd.ewma(df[ksgn], span = n_slow, min_periods = n_slow - 1))  
    MACD = pd.Series(EMAfast - EMAslow, name = xnam)  
    MACDsign = pd.Series(pd.ewma(MACD, span = 9, min_periods = 8), name =xnam2)  
    MACDdiff = pd.Series(MACD - MACDsign, name =xnam3)  
    df = df.join(MACD)  
    df = df.join(MACDsign)  
    df = df.join(MACDdiff)  
    return df
    



def MFI(df, n,ksgn='close'):   
    '''
    def MFI(df, n):					
    MFI,资金流量指标和比率,Money Flow Index and Ratio
　　资金流量指标又称为量相对强弱指标（Volume Relative Strength Index，VRSI），
	英文全名Money Flow Index，缩写为MFI，根据成交量来计测市场供需关系和买卖力道。
	该指标是通过反映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度
	来研判量能的趋势，预测市场供求关系和买卖力道，属于量能反趋向指标。	    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mfi_{n}，输出数据
    '''
    xnam='mfi_{d}'.format(d=n)
    PP = (df['high'] + df['low'] + df[ksgn]) / 3  
    i = 0  
    PosMF = [0]  
    while i <(len(df) - 1): #df.index[-1]:  
        if PP.iloc[i + 1] > PP.iloc[i]:  
            #PosMF.append(PP[i + 1] * df.get_value(i + 1, 'volume'))  
            PosMF.append(PP.iloc[i + 1] * df['volume'].iloc[i + 1])  
        else:  
            PosMF.append(0)  
        i = i + 1  
    #    
    PosMF = pd.Series(PosMF)  
    TotMF = PP * df['volume']  
    #MFR = pd.Series(PosMF / TotMF)  
    PosMF.index=TotMF.index
    MFR =PosMF / TotMF
    MFI = pd.Series(pd.rolling_mean(MFR, n), name = xnam)  
    #df = df.join(MFI)  
    #MFI.index=df.index;
    df[xnam]=MFI
    return df
    
def MOM(df, n,ksgn='close'):  
    '''
    
    def MOM(df, n,ksgn='close'):  
　　动量线，英文全名MOmentum，简称MOM。“动量”这一名词，市场上的解释相当广泛。以Momentum命名的指标，种类更是繁多。
		综合而言，动量可以视为一段期间内，股价涨跌变动的比率。
    
    动量指标.Momentum  
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mom_{n}，输出数据
    '''
    xnam='mom_{n}'.format(n=n)
    #M = pd.Series(df['close'].diff(n), name = 'Momentum_' + str(n))  
    M = pd.Series(df[ksgn].diff(n), name = xnam)  
    df = df.join(M)  
    return df
    



def MASS(df):  
    '''
    def MassI(df):					
    梅斯线（Mass Index）
　　梅斯线是Donald Dorsey累积股价波幅宽度之后，所设计的震荡曲线。
		本指标最主要的作用，在于寻找飙涨股或者极度弱势股的重要趋势反转点。
　　MASS指标是所有区间震荡指标中，风险系数最小的一个。		
    
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：mass，输出数据
    '''
    xnam='mass'
    Range = df['high'] - df['low']  
    EX1 = pd.ewma(Range, span = 9, min_periods = 8)  
    EX2 = pd.ewma(EX1, span = 9, min_periods = 8)  
    Mass = EX1 / EX2  
    MassI = pd.Series(pd.rolling_sum(Mass, 25), name = xnam)  #'Mass Index'
    df = df.join(MassI)  
    return df    
    



def OBV(df, n,ksgn='close'):   
    '''
    def OBV(df, n,ksgn='close'):   
    #能量潮指标（On Balance Volume，OBV）
    OBV指标是葛兰维（Joe Granville）于本世纪60年代提出的，并被广泛使用。
    股市技术分析的四大要素：价、量、时、空。OBV指标就是从“量”这个要素作为突破口，来发现热门股票、分析股价运动趋势的一种技术指标。
    它是将股市的人气——成交量与股价的关系数字化、直观化，以股市的成交量变化来衡量股市的推动力，从而研判股价的走势。
    关于成交量方面的研究，OBV能量潮指标是一种相当重要的分析指标之一。    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：obv_{n}，输出数据
        obv_x，放大10e6倍的输出数据
    '''
    xnam='obv_{d}'.format(d=n)
    i = 0  
    OBV = [0]  
    while i <  len(df) - 1:  #df.index[-1]
        #if df.get_value(i + 1, ksgn) - df.get_value(i, ksgn) > 0:  
        if df[ksgn].iloc[i+1]-df[ksgn].iloc[i] > 0:  
            #OBV.append(df.get_value(i + 1, 'Volume'))  
            OBV.append(df['volume'].iloc[i + 1])  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) == 0:  
            OBV.append(0)  
        if (df[ksgn].iloc[i+1]-df[ksgn].iloc[i]) < 0:  
            OBV.append(-df['volume'].iloc[i + 1])  
        i = i + 1  
    OBV = pd.Series(OBV)  
    OBV_ma = pd.Series(pd.rolling_mean(OBV, n), name = xnam)  
    #df = df.join(OBV_ma)  
    OBV_ma.index=df.index;
    df[xnam]=OBV_ma
    df['obv_x']=df[xnam]/10e6
    return df
    
    



def PPSR(df):  
    '''
    def PPSR(df):  					
     支点，支撑线和阻力线.Pivot Points, Supports and Resistances  
	PIVOT指标的观念很简单，不需要计算任何东西，它纯粹只是一个分析反转点的方法而已。
	PIVOT意思是指“轴心”，轴心是用来确认反转的基准，所以PIVOT指标其实就是找轴心的方法
     PIVOT指标，经常与布林带数据一起分析。

    【输入】
        df, pd.dataframe格式数据源
    【输出】    
        df, pd.dataframe格式数据源,
        增加了7栏：pp,s1,s2,s3,r1,r2,r3，输出数据
    '''
    PP = pd.Series((df['high'] + df['low'] + df['close']) / 3)  
    R1 = pd.Series(2 * PP - df['low'])  
    S1 = pd.Series(2 * PP - df['high'])  
    R2 = pd.Series(PP + df['high'] - df['low'])  
    S2 = pd.Series(PP - df['high'] + df['low'])  
    R3 = pd.Series(df['high'] + 2 * (PP - df['low']))  
    S3 = pd.Series(df['low'] - 2 * (df['high'] - PP))  
    psr = {'pp':PP, 'r1':R1, 's1':S1, 'r2':R2, 's2':S2, 'r3':R3, 's3':S3}  
    PSR = pd.DataFrame(psr)  
    df = df.join(PSR)  
    
    return df
    


def ROC(df, n,ksgn='close'):  

    '''
    def ROC(df, n,ksgn='close'):  
    变动率(Rate of change,ROC)
　　ROC是由当天的股价与一定的天数之前的某一天股价比较，其变动速度的大小,来反映股票市场变动的快慢程度。
		ROC，也叫做变动速度指标、变动率指标或变化速率指标。
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：_{n}，输出数据
    '''
    xnam='roc_{n}'.format(n=n)
    M = df[ksgn].diff(n - 1)  
    N = df[ksgn].shift(n - 1)  
    ROC = pd.Series(M / N, name = xnam)  
    df = df.join(ROC)  
    return df




def RSI(df, n):
    '''
    def RSI(df, n):  					
      #RSI，相对强弱指标,Relative Strength Index
	也称相对强弱指数、相对力度指数
	RSI，是通过比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走势。
	RSI通过特定时期内股价的变动情况计算市场买卖力量对比，来判断股票价格内部本质强弱、推测价格未来的变动方向的技术指标。

    【输入】
        df, pd.dataframe格式数据源
        n，时间长度,一般为14
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：rsi_{n}，输出数据
    '''
    xnam='rsi_{n}'.format(n=n)
    print( xnam)
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i]
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1]

        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    ds = pd.Series(PosDI / (PosDI + NegDI), name=xnam)
    #df = df.join(ds)
    #print('rsi')
    #print(len(ds),len(df))
    ds.index=df.index
    df[xnam]=ds*100
    return df



def RSI100(df, n):

    '''
    def RSI100(df, n):
        zw版RSI相对强弱指数，取0..100之间的数值
    
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        
    【输出】    
        df, pd.dataframe格式数据源,
        增加了2栏：rsi_{n}，输出数据
          rsi_k，中间输出数据
    '''    
    xnam='rsi_{n}'.format(n=n)
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]
        #UpMove = df.get_value(i + 1, 'high') - df.get_value(i, 'high')
        #DoMove = df.get_value(i, 'low') - df.get_value(i + 1, 'low')
        UpMove=df['high'].iloc[i+1]-df['high'].iloc[i];
        DoMove=df['low'].iloc[i]-df['low'].iloc[i+1];
        
        #Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else:
            UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else:
            DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = pd.Series(UpI)
    DoI = pd.Series(DoI)
    PosDI = pd.Series(pd.ewma(UpI, span=n, min_periods=n - 1))
    NegDI = pd.Series(pd.ewma(DoI, span=n, min_periods=n - 1))
    #ds = pd.Series(PosDI / (PosDI + NegDI))
    ds = pd.Series(PosDI / (PosDI + NegDI))
    ds.index=df.index
    #print(ds.tail())
    #df = df.join(ds)  
    #df[xnam]=ds;
    df['rsi_k']=ds;
    df[xnam]=100-100/(1+df['rsi_k']);
    
    return df
    


def STDDEV(df, n,ksgn='close'):
    '''
    def STDDEV(df, n,ksgn='close'):
    #标准偏差,#Standard Deviation
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：std_{n}，输出数据
    '''
    xnam='std_{d}'.format(d=n)
    df = df.join(pd.Series(pd.rolling_std(df[ksgn], n), name =xnam))  
    return df      
    
    

def STOD(df, n,ksgn='close'):    
    '''
    def STO(df, n,ksgn='close'):     
       随机指标D值,Stochastic oscillator %D  
	随机指标，又称KD指标，KDJ指标
　   随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。
　   KD指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。
　  随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价
  及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
  然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
       
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：_{n}，输出数据
    '''
    #xnam='stod'
    xnam='stod'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name = 'stok')
    SOd = pd.Series(pd.ewma(SOk, span = n, min_periods = n - 1), name = xnam)
    df = df.join(SOk) 
    df = df.join(SOd) 
    df['stod']=df['stod']*100
    df['stok']=df['stok']*100
    #print('n df',len(df))
    return df


def STOK(df,ksgn='close'):  
    '''
    def STOK(df,ksgn='close'):  
    随机指标K值,Stochastic oscillator %K
	随机指标，又称KD指标，KDJ指标
　   随机指标综合了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。
　   KD指标考虑的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。
　  随机指标一般是根据统计学的原理，通过一个特定的周期（常为9日、9周等）内出现过的最高价、最低价
  及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值RSV，
  然后根据平滑移动平均线的方法来计算K值、D值与J值，并绘成曲线图来研判股票走势。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：_{n}，输出数据
    '''
    xnam='stok'
    SOk = pd.Series((df[ksgn] - df['low']) / (df['high'] - df['low']), name =xnam)  
    df = df.join(SOk)  
    return df



def TRIX(df, n,ksgn='close'): 
    '''
    def TRIX(df, n,ksgn='close'): 
    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：trix_{n}，输出数据
    '''
    xnam='trix_{n}'.format(n=n)
    EX1 = pd.ewma(df[ksgn], span=n, min_periods=n - 1)
    EX2 = pd.ewma(EX1, span=n, min_periods=n - 1)
    EX3 = pd.ewma(EX2, span=n, min_periods=n - 1)
    i = 0
    ROC_l = [0]
    while i + 1 <= len(df) - 1:  # df.index[-1]:
        ROC = (EX3[i + 1] - EX3[i]) / EX3[i]
        ROC_l.append(ROC)
        i = i + 1
    trix  = pd.Series(ROC_l, name=xnam)
    #df = df.join(trix)     
    trix.index=df.index;
    df[xnam]=trix
     
    #print(trix.tail())
    #print('n',len(df))
    return df
    


def TSI(df, r, s,ksgn='close'):   
    
    '''
    def TSI(df, r, s,ksgn='close'):   
    TSI，真实强度指数,True Strength Index
  TSI是相对强弱指数 (RSI) 的变体。
  TSI 使用价格动量的双重平滑指数移动平均线，剔除价格的震荡变化并发现趋势的变化。
  r一般取25，是一般取13
    【输入】
        df, pd.dataframe格式数据源
        r,s，时间长度;  r一般取25，是一般取13
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：tsi，输出数据
    '''
    xnam='tsi'.format(d=r,d2=s)
    M = pd.Series(df[ksgn].diff(1))  
    aM = abs(M)  
    EMA1 = pd.Series(pd.ewma(M, span = r, min_periods = r - 1))  
    aEMA1 = pd.Series(pd.ewma(aM, span = r, min_periods = r - 1))  
    EMA2 = pd.Series(pd.ewma(EMA1, span = s, min_periods = s - 1))  
    aEMA2 = pd.Series(pd.ewma(aEMA1, span = s, min_periods = s - 1))  
    TSI = pd.Series(EMA2 / aEMA2, name = xnam)  
    df = df.join(TSI)  
    
    return df





#Ultimate Oscillator  
def ULTOSC(df,ksgn='close'):
    '''
    def ULTOSC(df,ksgn='close'):
    UOS，终极指标（Ultimate Oscillator，UOS）
　　终极指标，由拉瑞·威廉（Larry Williams）所创。他认为现行使用的各种振荡指标，对于周期参数的选择相当敏感。
   不同的市况，不同参数设定的振荡指标，产生的结果截然不同。因此，选择最佳的参数组含，成为使用振荡指标之前，最重要的一道手续。
　　为了将参数周期调和至最佳状况，拉瑞·威廉经过不断测试的结果，先找出三个周期不同的振荡指标，再将这些周期参数，按照反比例的方式，制作成常数因子。
   然后，依照加权的方式，将三个周期不同的振荡指标，分别乘以不同比例的常数，加以综合制作成UOS指标。
　　经过一连串参数顺化的过程后，UOS指标比一般单一参数的振荡指标，更能够顺应各种不同的市况。
    【输入】
        df, pd.dataframe格式数据源
        ksgn，列名，一般是：close收盘价
    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：uos，输出数据
    '''
    i = 0  
    TR_l = [0]  
    BP_l = [0]  
    xnam='uos'
    while i <  len(df) - 1:   #df.index[-1]:  
        #TR = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        TR = max(df['high'].iloc[i+1],df[ksgn].iloc[i])-min(df['low'].iloc[i+1],df[ksgn].iloc[i])  
        TR_l.append(TR)  
        #BP = df.get_value(i + 1, 'close') - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))  
        BP =df[ksgn].iloc[i+1]-min(df['low'].iloc[i+1], df[ksgn].iloc[i])  
        BP_l.append(BP)  
        i = i + 1  
    UltO = pd.Series((4 * pd.rolling_sum(pd.Series(BP_l), 7) / pd.rolling_sum(pd.Series(TR_l), 7)) + (2 * pd.rolling_sum(pd.Series(BP_l), 14) / pd.rolling_sum(pd.Series(TR_l), 14)) + (pd.rolling_sum(pd.Series(BP_l), 28) / pd.rolling_sum(pd.Series(TR_l), 28)), name =xnam)  # 'Ultimate_Osc'
    #df = df.join(UltO)      
    UltO.index=df.index;
    df[xnam]=UltO
    return df


def VORTEX(df, n):
    '''
    def VORTEX(df, n):
    螺旋指标,#Vortex Indicator  
    参见 http://www.vortexindicator.com/VFX_VORTEX.PDF


    
    【输入】
        df, pd.dataframe格式数据源
        n，时间长度

    【输出】    
        df, pd.dataframe格式数据源,
        增加了一栏：vortex__{n}，输出数据
    '''
    xnam='vortex_{n}'.format(n=n)
    i = 0
    TR = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = max(df.get_value(i + 1, 'high'), df.get_value(i, 'close')) - min(df.get_value(i + 1, 'low'), df.get_value(i, 'close'))
        Range=max(df['high'].iloc[i+1],df['close'].iloc[i])-min(df['low'].iloc[i+1],df['close'].iloc[i])
        #TR = max(df['High'].iloc[i + 1], df['Close'].iloc[i] - min(df['Low'].iloc[i + 1], df['Close'].iloc[i]))
        TR.append(Range)
        i = i + 1
    i = 0
    VM = [0]
    while i < len(df) - 1:  # df.index[-1]:
        #Range = abs(df.get_value(i + 1, 'high') - df.get_value(i, 'low')) - abs(df.get_value(i + 1, 'low') - df.get_value(i, 'high'))
        Range=abs(df['high'].iloc[i+1]-df['low'].iloc[i])-abs(df['low'].iloc[i+1]-df['high'].iloc[i])
        VM.append(Range)
        i = i + 1
    ds = pd.Series(pd.rolling_sum(pd.Series(VM), n) / pd.rolling_sum(pd.Series(TR), n), name=xnam)
    #df = df.join(ds)  
    ds.index=df.index;
    df[xnam]=ds
    
    return df




    
#=========================================


