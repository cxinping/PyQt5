# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:29:55 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from pandas import DataFrame

import os
import plotly.offline as pyof
import plotly.graph_objs as go
from plotly import figure_factory as ff


class Plotly_PyQt5():
    def __init__(self):
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
            
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir
    
    #path_plotly_four_line = os.getcwd() + os.sep + plotly_dir + os.sep + 'mpl_two_line.html'
    #pyof.plot_mpl(a, resize=True, auto_open=False, filename=path_plotly_four_line)

    def get_test_plot_path(self, file_name = 'test_plot.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        # Add data
        
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']
        high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
        low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
        high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
        low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
        high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
        low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
        
        # Create and style traces
        trace0 = go.Scatter(
            x = month,
            y = high_2014,
            name = 'High 2014',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                width = 4)
        )
        trace1 = go.Scatter(
            x = month,
            y = low_2014,
            name = 'Low 2014',
            line = dict(
                color = ('rgb(22, 96, 167)'),
                width = 4,)
        )
        trace2 = go.Scatter(
            x = month,
            y = high_2007,
            name = 'High 2007',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                width = 4,
                dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
        )
        trace3 = go.Scatter(
            x = month,
            y = low_2007,
            name = 'Low 2007',
            line = dict(
                color = ('rgb(22, 96, 167)'),
                width = 4,
                dash = 'dash')
        )
        trace4 = go.Scatter(
            x = month,
            y = high_2000,
            name = 'High 2000',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                width = 4,
                dash = 'dot')
        )
        trace5 = go.Scatter(
            x = month,
            y = low_2000,
            name = 'Low 2000',
            line = dict(
                color = ('rgb(22, 96, 167)'),
                width = 4,
                dash = 'dot')
        )
        data = [trace0, trace1, trace2, trace3, trace4, trace5]
        
        # Edit the layout
        layout = dict(title = 'Average High and Low Temperatures in New York',
                      xaxis = dict(title = 'Temperature (degrees F)'),
                      yaxis = dict(title = 'Month'),
                      )
        
        # Plot and embed in ipython notebook!
        fig = dict(data=data, layout=layout)
        pyof.plot(fig,  filename=path_plotly, auto_open=False)
        
        return path_plotly
    
    def get_plotly_path_period_return(self, file_name='period_return.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        
        本基金 = [-2.59,-2.59,-11.07,8.66,-5.84]
        沪深300 = [1.64,1.64,0.73,5.01,14.20]
        同类平均 = [-0.79,-0.79,-2.08,0.76,7.03]
        trace1 = go.Bar(
            x=['今年以来', '最近一个月', '最近三个月', '最近半年', '最近一年'],
            y=本基金,
            name='本基金'
        )
        trace2 = go.Bar(
            x=['今年以来', '最近一个月', '最近三个月', '最近半年', '最近一年'],
            y=沪深300,
            name='沪深300'
        )
        
        trace3 = go.Bar(
            x=['今年以来', '最近一个月', '最近三个月', '最近半年', '最近一年'],
            y=同类平均,
            name='同类平均'
        )
        
        data = [trace1, trace2, trace3]
        layout = go.Layout(
            barmode='group'
        )
        
        fig = go.Figure(data=data, layout=layout)
        pyof.plot(fig,  filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_lagest_back(self, file_name='lagest_back.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        
        lagest_down = [-3.74, -3.736, -3.736, -5.969, -5.969]
        lagest_back = [-6.29, -6.285, -6.042, -11.651, -13.942]
        
        std = [10.271, 8.552, 9.123, 10.839, 10.529]
        
        xticks = ['2016/9', '2016/10','2016/11','2016/12','2017/1',]
        
        trace1 = go.Bar(
            x=xticks,
            y=lagest_down,
            name='最大下跌'
        )
        trace2 = go.Bar(
            x=xticks,
            y=lagest_back,
            name='最大回撤'
        )
        
        data = [trace1, trace2]
        layout = go.Layout(barmode='group')
        
        fig = go.Figure(data=data,layout=layout)
        pyof.plot(fig,  filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_month_return(self, file_name='month_return.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name        
                
        date = ['2017-01', '2016-12', '2016-11', '2016-10', '2016-09', '2016-08', '2016-07', '2016-06',
                '2016-05', '2016-04', '2016-03', '2016-02', '2016-01', '2015-12', '2015-11', '2015-10' ]
        
        ret = [-2.59, -5.97, -2.91, -0.39, -2.78, 6.07, 0.49, -0.32, 2.78, 0.01, 0.58, -0.46, -3.74, 0.75, 0.37, 6.08]
        data = [go.Bar(
                    x=date,
                    y=ret,
                name = '月度收益'
            )]
        
        pyof.plot(data,  filename=path_plotly, auto_open=False)
        return path_plotly
    
    def get_plotly_path_product_vs_hs300(self, file_name='product_vs_hs300.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name        
                
        data = pd.read_excel(r'data\和聚光明1号_hs300_merge.xlsx', index_col=[0]
                             )
        data.rename_axis(lambda x: pd.to_datetime(x), inplace=True)
        data.dropna(inplace=True)
        
        data = [
            go.Scatter(
                x=data.index, # assign x as the dataframe column 'x'
                y=data.cumulative_nav,
                name='和聚光明1号'
            ),
            go.Scatter(
                x=data.index, # assign x as the dataframe column 'x'
                y=data.close,
                name='沪深300'
            )
        ]
        pyof.plot(data,  filename=path_plotly, auto_open=False)
        return path_plotly


    def get_plotly_path_monte_markovitz(self, file_name='monte_markovitz.html',monte_count=400,risk_free = 0.03):
        """
        """
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        df = pd.read_excel(r'data\组合.xlsx',index_col=[0])
        returns = df.pct_change()
        returns.dropna(inplace=True)
        noa = 3

        # 蒙特卡洛随机模拟结果
        port_returns = []
        port_variance = []

        for p in range(monte_count):
            weights = np.random.random(noa)
            weights /= np.sum(weights)
            port_returns.append(np.sum(returns.mean() * 50 * weights)) # 加入模拟的均值
            port_variance.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 50, weights)))) # 加入模拟的标准差

        port_returns = np.array(port_returns)
        port_variance = np.array(port_variance)
        color_array = (port_returns - risk_free) / port_variance # 夏普比，不同的夏普比对应的颜色是不同的。

        trace1 = go.Scatter(
            x=port_variance,
            y=port_returns,
            mode='markers',
            marker=dict(
                size='6',
                color=color_array,  # 通过一个可变的变量表示颜色，结果是绘图颜色可变。
                colorscale='Viridis',
                # 设置colorbar
                colorbar=dict(
                    tickmode='linear',
                    tick0=color_array.min(),
                    dtick=(color_array.max() - color_array.min()) / 5,
                ),
                showscale=True,
            )
        )
        data = [trace1]

        pyof.plot(data, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_table(self,file_name='产品组合信息表.html',df=None,w=None):
        '''画产品组合信息表
        df为dataframe，末尾一列为组合。
        w为权重
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        risk_free = 0.03
        std_year = df.std() * 50
        mean_year = df.pct_change().mean() * 50 - risk_free
        sharp_year = mean_year / std_year
        max_drawback = (df / df.cummax()).min()

        _temp = {i[0]: i[1] for i in zip(['风险', '均值', '夏普比', '最大回撤'], [std_year, mean_year, sharp_year, max_drawback])}
        df_info = pd.concat(_temp, axis=1).T
        df_info.index.name = '指标'
        df_info = df_info.round(decimals=3)
        table = ff.create_table(df_info, index=True, index_title='指标')


        pyof.plot(table, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_pie(self,file_name='产品组合成分饼图.html',df=None,w=None):
        '''
        画产品组合成分饼图
        df为dataframe，末尾一列为组合。
        w为权重
        :return:
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name

        labels = df.columns[:-1]
        values = w
        trace = go.Pie(labels=labels, values=values, text='哈哈')
        layout = dict(title='产品组合成分图')
        fig = dict(data=[trace], layout=layout)


        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_versus(self,file_name='产品组合VS沪深300.html',df=None,df_base=None,w=None):
        '''
        画产品组合VS沪深300
        df为dataframe，末尾一列为组合。
        w为权重
        :return:
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name

        df_contra = pd.concat([df_base.close, df['组合']], axis=1, join='inner')
        df_contra = df_contra / df_contra.iloc[0, :]
        df_contra.rename(columns={'close': '沪深300'}, inplace=True)

        trace1 = go.Scatter(x=df_contra.index, y=df_contra.iloc[:, 0], mode='lines+markers',
                            name='沪深300', marker=dict(color='blue'))
        trace2 = go.Scatter(x=df_contra.index, y=df_contra.iloc[:, 1], mode='lines+markers',
                            name='产品组合', marker=dict(color='red'))
        data = [trace1, trace2]
        layout = {'title': '产品组合VS沪深300'}
        fig = dict(data=data, layout=layout)

        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

