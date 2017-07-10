# -*- coding: utf-8 -*-
"""
She35 Editor

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from pandas import DataFrame
import os

def get_markov(path_list,risk_free = 0.03):
    '''

    :param path_list:
    :return: df : 相对净值
            opts.x：sharp最优的权重。
    '''

    ser_list = [] # 存放Series的list，用来合并成DataFrame
    for path in path_list:
        path_name = path.split(os.sep)[-1][:-4] # 获取文件名
        _df = pd.read_csv(path, encoding='gbk', index_col=['price_date'], parse_dates=['price_date'])
        _ser = _df['nav'] # 获取净值
        _ser.name = path_name # 对Series重命名
        _ser.drop_duplicates(inplace=True) # 去重
        ser_list.append(_ser)


    df = pd.concat(ser_list,axis=1,join='outer') # 合并ser_list里面的Series
    df.sort_index(ascending=True, inplace=True)
    df.fillna(method='ffill',inplace=True) # 以前值来填充缺失值，因为不同产品的公布时间不同，所以在某个时间点对某个产品会存在缺失值现象

    df.dropna(inplace=True) # 去掉缺失值，考虑第一行为缺失值的情况。
    df = df / df.iloc[0, :] # 净值归一化。


    return df,w


if __name__ == '__main__':
    path_list = [r'data\昆仑信托-昆仑三十六号.csv',
                 r'data\时时安稳健1号.csv',
                 r'data\长城国瑞证券恒通23号.csv']

    df,w = get_markov(path_list)


    '''画产品组合信息表'''
    df['组合'] = (df * w).sum(axis=1)
    risk_free = 0.03

    std_year = df.std() * 50
    mean_year = df.pct_change().mean() * 50 - risk_free
    sharp_year = mean_year / std_year
    max_drawback = (df / df.cummax()).min()

    _temp = {i[0]:i[1] for i in zip(['风险', '均值', '夏普比','最大回撤'],[std_year, mean_year, sharp_year, max_drawback])}
    df_info = pd.concat(_temp,axis=1).T
    df_info.index.name = '指标'
    df_info = df_info.round(decimals=3)

    import plotly.offline as pyof
    from plotly import figure_factory as ff
    table = ff.create_table(df_info,index=True, index_title='指标')
    pyof.plot(table, filename='产品组合信息表.html')


    '''画饼图'''
    import plotly.graph_objs as go

    labels=df_info.columns[:-1]
    values=w
    trace=go.Pie(labels=labels,values=values,text='哈哈')
    layout = dict(title = '产品组合成分图')
    fig = dict(data=[trace],layout=layout)
    pyof.plot(fig,filename='组合成分图.html')


    '''画产品对比图'''
    import tushare as ts
    data_hs300 = ts.get_hist_data('hs300')
    data_hs300 = data_hs300.rename_axis(lambda x:pd.to_datetime(x))
    df_contra = pd.concat([data_hs300.close,df['组合']],axis=1,join='inner')
    df_contra = df_contra / df_contra.iloc[0,:]
    df_contra.rename(columns={'close':'沪深300'},inplace=True)


    import plotly.graph_objs as go
    trace1 = go.Scatter(x=df_contra.index,y=df_contra.iloc[:,0],mode = 'lines+markers',
        name = '沪深300',marker=dict(color='blue'))
    trace2 = go.Scatter(x=df_contra.index,y=df_contra.iloc[:,1],mode = 'lines+markers',
        name = '产品组合',marker=dict(color='red'))
    data = [trace1,trace2]
    layout = {'title' : '产品组合VS沪深300'}
    fig = dict(data=data,layout=layout)
    pyof.plot(fig,filename='产品组合VS沪深300.html')