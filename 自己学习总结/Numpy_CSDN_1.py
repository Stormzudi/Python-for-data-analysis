# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 16:18
# @Author  : Zudy
# @FileName: Numpy_CSDN_1.py

'''
1.实现类型的转换：
   Ndarray转换成Dataframe
   Dataframe转换成Ndarray
'''

import numpy as np
import pandas as pd


# Ndarray转换成Dataframe
mat = np.random.randn(4,4)
df = pd.DataFrame(mat)
df.columns = ['a', 'b', 'c', 'd']  # 修改DataFrame的列明

print(df)

# Dataframe转换成Ndarray
df = pd.DataFrame(
    {'A':[1,2,3],
     'B':[4,5,6],
     'C':[7,8,9]})

data_1 = df.values
data_2 = df.as_matrix()
data_3 = np.array(df)

print(type(data_1))
print(data_2)
print(data_3)
