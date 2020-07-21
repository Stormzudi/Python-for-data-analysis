# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 23:25
# @Author  : Zudy
# @FileName: Course5_Pandas_3.py
'''
1. 关于CSDN中pandas模块的撰写
'''
import pandas as pd
import numpy as np

obj = pd.Series([4, 5, -1, 3])
print(obj)

val = pd.Series([-1.2,-1.5,-1.7],
                index=['one','two','three'])
print(val)


data = {
    'chinese': [75, 68, 54, 55, 59, 45, 61],
    'english': [69, 85, 42, 57, 35, 63, 53],
    'math': [36, 87, 59, 63, 92, 92, 76],
    'name': ['a', 'b', 'c', 'd', 'e', 'e', 'f'],
    'test': [1, 1, 1, 2, 2, 3, 1]
}
df = pd.DataFrame(data,columns=['chinese','english','math','name','test'])
print(df)


path = 'D:/Python/Python_learning/HBUT/预处理/data1.xlsx'
df1 = pd.read_excel(path)
data = df1.ix[0,1]
print(df1.head())
print(data)