# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 15:20
# @Author  : Zudy
# @FileName: Numpy_CSDN_3.py
'''
1.数组的拆分与合并
'''

import numpy as np


arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]])

arr_1 = np.split(arr, 2, axis=1)  # 纵向分2部分
arr_2 = np.split(arr, 3, axis=0)  # 横向分3部分
arr_3 = np.array_split(arr, 2, axis=1)  # 纵向分3部分
arr_4 = np.vsplit(arr, 3) # 横着分3组
arr_5 = np.hsplit(arr,2)  # 竖着分2组


print(arr_1)
print(arr_1[0])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
a1 = np.vstack((arr1, arr2))
a2 = np.hstack((arr1, arr2))
print(a1)
print(a2)


arr1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]])
arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]])

b1 = np.concatenate((arr1, arr2), axis=0)  #在纵轴上合并
b2 = np.concatenate((arr1, arr2), axis=1)  #在纵轴上合并

print(b1)
print(b2)



