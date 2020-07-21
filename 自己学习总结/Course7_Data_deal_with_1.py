# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 20:50
# @Author  : ZhuNian
# @FileName: Course3_Data_deal_with_1.py
# @Software: PyCharm

'''
7.1 处理缺失数据
    7.1.1滤除缺失数据
    7.1.2填充缺失数据
7.2 数据转换
    7.2.1移除重复数据
    7.2.2利用函数或映射进行数据转换
    7.2.3替换值
    7.2.4重命名轴索引
    7.2.5离散化和面元划分
    7.2.6检测和过滤异常值
    7.2.7排列和随机采样
    7.2.8计算指标/哑变量
7.3 字符串操作
    7.3.1字符串对象方法
    7.3.2正则表达式
    7.3.3pandas的矢量化字符串函数
'''
import pandas as pd
import numpy as np


print('~~~~~~~~~~~~~~~~~~~~~~7.1~~~~~~~~~~~~~~~~~~~~~~')
#7.1 处理缺失数据
#对于数值数据，pandas使用浮点值NaN（Not a Number）表示缺失数据
string_data = pd.Series(['aardvark', 'artichoke', None, 'avocado'])
print(string_data)
print(string_data.isnull()) #isnull()表示那个值是否为缺失值


print('~~~~~~~~~~~~~~~~~~~~~~7.1.1~~~~~~~~~~~~~~~~~~~~~~')

#滤除缺失数据t
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
r = data.dropna() #dropna返回一个仅含非空数据和索引值的Series
t = data[data.notnull()] #与dropna()等价
print(r)
print(t)

#而对于DataFrame对象，事情就有点复杂了,
# dropna默认丢弃任何含有缺失值的行
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
print(data)
print(cleaned)
#如果只想丢弃全部是NAN的行
cleaned = data.dropna(how='all')
print(cleaned)
#如果只想丢弃全部是NAN的列
data[4] = NA
cleaned = data.dropna(axis= 1,how='all')
print(cleaned)

#假设你只想留下一部分观测数据，可以用thresh参数实现此目的
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] =NA
df.iloc[:2, 2] =NA
print(df)
r = df.dropna(thresh=2)
print(r)

print('~~~~~~~~~~~~~~~~~~~~~~7.1.2~~~~~~~~~~~~~~~~~~~~~~')
#7.1.2填充缺失数据
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] =NA
df.iloc[:2, 2] =NA
r = df.fillna(0)
print(r)
#若是通过一个字典调用fillna，就可以实现对不同的列填充不同的值：
r = df.fillna({1:0.5, 2:0})
print(r)

#就可以利用fillna实现许多别的功能。比如说，你可以传入Series的平均值或中位数：
data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())
print(data)