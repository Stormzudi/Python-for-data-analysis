# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 21:12
# @Author  : ZhuNian
# @FileName: course_DataFrame_2.py
# @Software: PyCharm

'''
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


#5.2修改数据
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2015,2016,2017,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame2 = pd.DataFrame(data,index=['one','two','three','four','five'],columns=['year','state','pop','debt'])
print(frame2)
frame2['debt'] = 1 #修改 frame中debt列one行的元素
print(frame2)
# frame2['debt']['one'] = 1 #修改 frame中debt列one行的元素
# print(frame2)

#也可以使用一个列表来修改，不过要保证列表的长度与DataFrame长度相同：
frame2.debt = np.arange(5)
print(frame2)

#可以使用一个Series，此时会根据索引进行精确匹配：
val = pd.Series([-1.2,-1.5,-1.7],
                index=['two','four','five'])  #讲-1.2替换到two上，
frame2['debt'] = val

print(val)
print(frame2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.3.重新索引
#使用reindex方法对DataFrame进行重新索引。对DataFrame进行重新索引，可以重新索引行，列或者两个都修改，如果只传入一个参数，则会从新索引行：
frame1 = pd.DataFrame(np.arange(9).reshape((3,3)),index=[1,4,5],columns=['Ohio','Texas','California'])
frame2 = frame1.reindex([1,2,4,5]) #增加一行为‘2’
print(frame2)

states = ['Texas','Utah','California','haha']
frame2 = frame1.reindex(columns=states)
print(frame2)

#填充数据只能按行填充，此时只能对行进行重新索引
frame1 = pd.DataFrame(np.arange(9).reshape((3,3)),index = ['a','c','d'],columns = ['Ohio','Texas','California'])
frame2 = frame1.reindex(['a','b','c','d'], method = 'bfill')
# frame.reindex(['a','b','c','d'],method = 'bfill',columns=states) #报错
print(frame2)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.4 丢弃指定轴上的值
#可以使用drop方法丢弃指定轴上的值，不会对原DataFrame产生影响
frame = pd.DataFrame(np.arange(9).reshape((3,3)),index = ['a','c','d'],columns = ['Ohio','Texas','California'])
frame2 = frame.drop('a')
print(frame)
print(frame2)

frame2 = frame.drop(['Ohio'], axis=1)  #axis=1 表示行 axis=0表示列
print(frame2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.5.算术运算
#DataFrame在进行算术运算时会进行补齐，在不重叠的部分补足NA：
df1 = pd.DataFrame(np.arange(9).reshape((3,3)),index=list('bcd'),columns=['Ohio','Texas','Colorado'])
df2 = pd.DataFrame(np.arange(12).reshape((3,4)),index = list('bde'),columns=['Utah','Ohio','Texas','Oregon'])
frame = df1 + df2
print(df1)
print(df2)
print(frame)

#可以使用fill_value方法填充NA数据，不过两个df中都为NA的数据，该方法不会填充：
frame = df1.add(df2,fill_value=0)
print(frame)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.6.函数应用和映射
#numpy的元素级数组方法，也可以用于操作Pandas对象:
frame = pd.DataFrame(np.random.randn(3,3),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
r = np.abs(frame)
print(r)

#另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上。DataFrame的apply方法即可实现此功能。
f = lambda x: x.max() - x.min()
frame.apply(f, axis=1)
print(frame)
frame.apply(f,axis=0)
print(frame)

#另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上。DataFrame的apply方法即可实现此功能。
def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
r = frame.apply(f)
print(r)

#元素级的Python函数也是可以用的,使用applymap方法:
format = lambda x:'%.2f'%x
r = frame.applymap(format)
print(r)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#5.7.排序和排名
#对于DataFrame,sort_index可以根据任意轴的索引进行排序，并指定升序降序
frame = pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
r = frame.sort_index()
print(r)
r = frame.sort_index(1,ascending=False)
print(r)

#DataFrame也可以按照值进行排序：
r = frame.sort_values(by=['a','b'])
print(r)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.8汇总和计算描述统计
#DataFrame中的实现了sum、mean、max等方法,我们可以指定进行汇总统计的轴，同时，也可以使用describe函数查看基本所有的统计项：
df = pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
df.sum(axis=1)

#Na会被自动排除，可以使用skipna选项来禁用该功能
df.mean(axis=1,skipna=False)

#idxmax返回间接统计，是达到最大值的索引
df.idxmax()


#describe返回的是DataFrame的汇总统计
#非数值型的与数值型的统计返回结果不同
df.describe()

#DataFrame也实现了corr和cov方法来计算一个DataFrame的相关系数矩阵和协方差矩阵，同时DataFrame也可以与Series求解相关系数。
frame1 = pd.DataFrame(np.random.randn(3,3),index=list('abc'),columns=list('abc'))
r = frame1.corr
r = frame1.cov()

#corrwith用于计算每一列与Series的相关系数
frame1.corrwith(frame1['a'])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.9.处理缺失数据
#Pandas中缺失值相关的方法主要有以下三个：
# isnull方法用于判断数据是否为空数据；
# fillna方法用于填补缺失数据；
# dropna方法用于舍弃缺失数据。
# 上面两个方法返回一个新的Series或者DataFrame，对原数据没有影响,如果想在原数据上进行直接修改，使用inplace参数：
data = pd.DataFrame([[1,6.5,3],[1,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3]])
data.dropna()

#对DataFrame来说，dropna方法如果发现缺失值，就会进行整行删除，不过可以指定删除的方式，how=all，是当整行全是na的时候才进行删除,同时还可以指定删除的轴。
data.dropna(how='all',axis=1,inplace=True)

#DataFrame填充缺失值可以统一填充，也可以按列填充，或者指定一种填充方式：
data.fillna({1:2,2:3})
data.fillna(method='ffill')
