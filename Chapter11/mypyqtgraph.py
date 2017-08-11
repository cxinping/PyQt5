'''
ParameterTree的主函数，用来显示基金产品的文本/数值信息
'''

import copy
import pickle
from pyqtgraph.parametertree import Parameter


# 创建参数树的数据
params = [
    {'name': '基本收益信息', 'type': 'group', 'children': [
        {'name': '今年收益', 'type': 'float', 'value': -2.45, 'siPrefix': True, 'suffix': '%'},
        {'name': '累计收益', 'type': 'float', 'value': -2.72, 'step': 0.1, 'siPrefix': True, 'suffix': '%'},
        {'name': '最近净值日期', 'type': 'str', 'value': "2017-02-03"},
        {'name': '最新净值', 'type': 'float', 'value': 0.9728, 'step': 0.01},
        {'name': '累计净值', 'type': 'float', 'value': 0.9728, 'step': 0.01},
    ]},
    {'name': '基本产品信息', 'type': 'group', 'children': [
        {'name': '开放日', 'type': 'str', 'value': '6个月'},
        {'name': '累计收益', 'type': 'str', 'value': '封闭期后，每个自然季度的最后一个月的20日至22日'},
        {'name': '认购起点', 'type': 'float', 'value': 100.00, 'step': 10, 'siPrefix': True, 'suffix': '万(人民币)'},
        {'name': '追加起点', 'type': 'float', 'value': 10.00, 'step': 1, 'siPrefix': True, 'suffix': '万(人民币)'},
        {'name': '认购费率', 'type': 'float', 'value': 1.00, 'step': 0.1, 'siPrefix': True, 'suffix': '%'},
        {'name': '赎回费率', 'type': 'float', 'value': 0, 'step': 0.1},
        {'name': '预警线', 'type': 'float', 'value': 85, 'step': 1, 'siPrefix': True, 'suffix': '%'},
        {'name': '止损线', 'type': 'float', 'value': 80, 'step': 1, 'siPrefix': True, 'suffix': '%'},
    ]},

    {'name': '投顾信息', 'type': 'group', 'children': [
        {'name': '投资顾问', 'type': 'str', 'value': '和聚投资'},
        {'name': '业绩报酬', 'type': 'float', 'value': 20, 'step': 1, 'siPrefix': True, 'suffix': '%'},
        {'name': '基金管理人', 'type': 'str', 'value': '千石资本'},
        {'name': '管理人管理费', 'type': 'str', 'value': '0'},
        {'name': '基金托管人', 'type': 'str', 'value': '光大银行'},
        {'name': '证券经纪商', 'type': 'str', 'value': '未设'},
        {'name': '期货经纪商', 'type': 'str', 'value': '未设'},
    ]},
    {'name': '其他信息', 'type': 'group', 'children': [
        {'name': '成立日期', 'type': 'str', 'value': '2015-08-04'},
        {'name': '是否分级', 'type': 'str', 'value': '否'},
        {'name': '产品类型', 'type': 'str', 'value': '公募专属'},
        {'name': '投资策略', 'type': 'str', 'value': '股票策略'},
        {'name': '子策略', 'type': 'str', 'value': '股票多头'},

    ]},
]


## 创建参数对象树
p = Parameter.create(name='params', type='group', children=params)


## 若树里面的任何内容发生变化，则输出这些变化
def change(param, changes):
    print("tree changes:")
    for param, change, data in changes:
        path = p.childPath(param)
        if path is not None:
            childName = '.'.join(path)
        else:
            childName = param.name()
        print('  parameter: %s' % childName)
        print('  change:    %s' % change)
        print('  data:      %s' % str(data))
        print('  ----------')


p.sigTreeStateChanged.connect(change)


def valueChanging(param, value):
    print("Value changing (not finalized):", param, value)


# Too lazy for recursion:
for child in p.children():
    child.sigValueChanging.connect(valueChanging)
    for ch2 in child.children():
        ch2.sigValueChanging.connect(valueChanging)


