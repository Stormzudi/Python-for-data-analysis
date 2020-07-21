# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 18:06
# @Author  : ZhuNian
# @FileName: course1_DataFrame.py
# @Software: PyCharm

'''
1.DataFrame是一种表格型数据结构，它含有一组有序的列，每列可以是不同的值。
  DataFrame既有行索引，也有列索引，它可以看作是由Series组成的字典，不过这些Series公用一个索引。
  DataFrame的创建有多种方式，不过最重要的还是根据dict进行创建，以及读取csv或者txt文件来创建。
2.创建方法：
  1.根据字典创建
  2.我们可以在创建DataFrame时指定索引的值。
  3.使用嵌套字典也可以创建DataFrame，此时外层字典的键作为列，内层键则作为索引。
3.索引访问
4.DataFrame轴的概念
5.DataFrame一些性质
     1.索引、切片
     2.修改数据
     3.重新索引
     4.丢弃指定轴上的值
     5.算术运算
     6.函数应用和映射
     7.排序和排名
     8.汇总和计算描述统计
     9.处理缺失数据
'''

import pandas as pd
import numpy as np


#2.1根据字典创建
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame = pd.DataFrame(data)
print(type(frame))  #<class 'pandas.core.frame.DataFrame'>类型
print(frame)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#2.2 DataFrame的行索引是index，列索引是columns，我们可以在创建DataFrame时指定索引的值。
frame2 = pd.DataFrame(data,
                      index=['one','two','three','four','five'],
                      columns=['year','state','pop','debt'])    #debt 没有定义故为空值
print(type(frame2))  #<class 'pandas.core.frame.DataFrame'>类型
print(frame2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#2.3 使用嵌套字典也可以创建DataFrame，此时外层字典的键作为列，内层键则作为索引。
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = pd.DataFrame(pop)
print(type(frame3))  #<class 'pandas.core.frame.DataFrame'>类型
print(frame3)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#3.访问索引：
#我们可以用index（行索引），columns（列索引），values（数据值）来访问DataFrame的行索引，列索引以及数据值
# 数据值返回的是一个二维的ndarray
print(frame2.index)
print(frame2.columns)
print(frame2.values)  #二维的ndarray矩阵
# print(frame2.values[1][1])



#读取文件生成DataFrame最常用的是read_csv, read_table， read_excel方法。

#4.DataFrame轴的概念:
#在 DataFrame的处理中经常会遇到轴的概念，这里先给大家一个直观的印象，我们所说的
# axis=0即表示沿着每一列或行标签\索引值向下执行方法，
# axis=1即表示沿着每一行或者列标签模向执行对应的方法。

print('~~~~~~~~~~~~~~~~~~~5.1~~~~~~~~~~~~~~~~~~')
#5.DataFrame一些性质
#5.1.索引、切片
print(type(frame2['year']))  #<class 'pandas.core.series.Series'> 类型
print(frame2['year'])  #我们可以根据列名来选取一列，返回一个Series


#我们还可以选取多列或者多行
data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index = ['Ohio','Colorado','Utah','New York'],
                    columns=['one','two','three','four'])
row_1 = data[1:2]  #取单行
row_2 = data[:2]  #取多行
col = data[['one','two']] #取多列
print(data)
print(type(row_1),type(row_2))
print(row_1)
print(row_2)
print(col)

#当然，在选取数据的时候，我们还可以根据逻辑条件来选取
r_1 = data[data['three']>5]
print(r_1)

#pandas提供了专门的用于索引DataFrame的方法，即使用ix方法进行索引,不过ix在最新的版本中已经被废弃了，
#如果要是用标签，最好使用loc方法，如果使用下标，最好使用iloc方法：
#data.ix['Colorado',['two','three']]
r_2 = data.loc['Colorado',['two','three']]  #如果要是用标签
r_3 = data.iloc[0:3,2]  #如果使用下标，最好使用iloc方法
print(r_2)
print(r_3)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


