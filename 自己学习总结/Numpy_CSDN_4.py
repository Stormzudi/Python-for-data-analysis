# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 16:25
# @Author  : Zudy
# @FileName: Numpy_CSDN_4.py
'''
1.统计方法
2.排序
'''

import numpy as np

a = np.arange(9).reshape((3,3))
r1 = np.amin(a, axis=0)
r2 = np.amin(a, axis=1)
r3 = np.amax(a, axis=0)
r4 = np.amax(a, axis=1)

print(a)
print(r2)
print(r3)
print(r4)

r1 = np.median(a, axis=0)
r2 = np.median(a, axis=1)
r3 = np.mean(a, axis=0)
r4 = np.mean(a, axis=1)

print(r1)
print(r2)
print(r3)
print(r4)


r1 = np.std(a, axis=0)
r2 = np.std(a, axis=1)
print(r1)
print(r2)
print(np.std(a[:, 0]))

r1 = np.var(a, axis=0) # 沿列轴计算方差
r2 = np.var(a, axis=1) # 沿行轴计算方差
print(r1)
print(r2)


arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[10, 20, 70], [50, 20, 10]]
arr1 = np.array(arr1)
arr2 = np.array(arr2)
correlation = np.corrcoef(arr1, arr2)
correlation_1 = np.cov(arr1, arr2)
print("相关系数矩阵=\n", correlation)
print("相关系数矩阵=\n", correlation_1)


arr = np.random.randn(6)
print(arr)
arr.sort()
print(arr)

arr = np.random.randn(5, 3)
arr.sort(1)


print('~~~~~~~~~~~~~~~ lexsort 函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 录入了四位同学的成绩，按照总分排序，总分相同时语文高的优先
math    = (10, 20, 50, 10)
chinese = (30, 50, 40, 60)
total   = (40, 70, 90, 70)
# 将优先级高的项放在后面
ind = np.lexsort((math, chinese, total))
print(ind)

for i in ind:
    print(total[i],chinese[i],math[i])
    
list1 = [[4,3,2],[2,1,4]]
array=np.array(list1)
# array.sort(axis=1)  # axis=1,说明是按照行进行排序，也就是说，每一行上的元素实现了递增
array.sort(axis=0)  # axis=0,说明是按照列进行排序，也就是说，每一列上的元素实现了递增
print(array)
# print(r2)

a = [1, 5, 1, 4, 3, 4, 4]
b = [9, 4, 0, 4, 0, 2, 1]
data = np.lexsort((b, a))
print(data)

