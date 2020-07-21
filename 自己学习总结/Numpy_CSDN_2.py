# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 11:41
# @Author  : Zudy
# @FileName: Numpy_CSDN_2.py

'''
1.数组的索引和切片
2.数组重塑
'''

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
data_1 = arr[0][2]  # 选取单个元素
data_2 = arr[0, 2]  # 选取单个元素
print(data_1)
print(data_2)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
data_1 = arr[:2, 1:]
data_2 = arr[2, :]
data_3 = arr[:, :2]
data_4 = arr[1, :2]
print(data_1)
print(data_2)
print(data_3)
print(data_4)


arr = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]])
# arr.shape = (4, 3)
arr.shape = (2, -1)
print(arr)


arr = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]])
arr_1 = arr.reshape(-1, 1)  # 重塑一列
arr_2 = arr.reshape(1, -1)  # 重塑一行
arr_3 = arr.reshape(2, 6)   # 重塑一行

print(arr_1)
print(arr_2)
print(arr_3)


