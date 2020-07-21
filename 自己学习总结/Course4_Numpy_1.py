# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 19:23
# @Author  : ZhuNian
# @FileName: numpy_1.py
# @Software: PyCharm

'''
1.NumPy 的 ndarray：一种多维数组对象
2.NumPy 数组的运算
3.基本的索引和切片
4.切片索引
5.布尔型索引
6.数组转置和轴对换
'''

import numpy as np

# 1.NumPy 的 ndarray：一种多维数组对象
data = np.random.rand(2,3)
print(data)
print(data * 10) # 所有的元素都乘以 10
print(data + data)  # 所有的元素相加
print(data[1][1])  # 返回data[1][1]的值

# 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data2)
print(type(data2))  # <class 'list'>
print(type(arr))  # <class 'numpy.ndarray'>
print(arr.ndim)  # 返回几个维度
print(arr.shape)  # 返回矩阵的维度

# 数据类型保存在一个特殊的 dtype 对象中
print(arr.dtype)
float_arr = arr.astype(np.float64)  #将int型的数据类型转变成float类型
#arr.astype(np.int32)
print(float_arr)
print(float_arr.dtype)

#zeros 和 ones 分别可以创建指定长度或形状的全 0 或全 1 数组
r = np.zeros(10)
r = np.zeros((3, 6))
r = np.empty((2, 3, 2))
r = np.ones(5)
print(r)

#如果某字符串数组表示的全是数字，也可以用 astype 将其转换为数值形式：
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
numeric_strings.astype(float)  #注意这里可写成 float,而不是np.float
print(numeric_strings)

#可以用其他数组的dtype直接来制定类型：
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)

empty_uint32 = np.empty(8, dtype='u4') #还可以利用类型的缩写，比如u4就代表unit32
print(empty_uint32)

print('~~~~~~~~~~~~~~~~~~~~~2222222~~~~~~~~~~~~~~~~~~~~~~~~~~')

#2.NumPy 数组的运算
#数组很重要，因为它使你不用编写循环即可对数据执行批量运算。NumPy 用户称其为矢量化（vectorization）。
#大小相等的数组之间的任何算术运算都会将运算应用到元素级：

arr = np.array([[1,2,3],[4,5,6]], dtype= np.int32)
print(arr)
print(arr + arr)
print(arr * arr)

#数组与标量的算术运算会将标量值传播到各个元素：
print( 1 / arr)
print(arr *  0.5)
# print((arr *  0.5).dtype) #浮点型

#大小相同的数组之间的比较会生成布尔值数组：
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)


print('~~~~~~~~~~~~~~~~~~~~~3333333~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 3.基本的索引和切片

arr = np.arange(10)
r = arr[5:8]
print(r)
arr[5:8] = 12
print(arr)

# 在，当我修稿 arr_slice 中的值，变动也会体现在原始数组 arr 中：
r[1] = 1234   # 视图上的任何修改都会直接反映到源数组上
print(arr)

#切片 [:] 会给数组中的所有值赋值：
arr[:] = 1
print(arr)

#如果想得到的是数值的复制而不是视图时
r = arr[5:8].copy()

#对于高维度数组，能做的事情更多。在一个二维数组中，各索引位置上的元素不再是标量而是一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])

#各个元素进行递归访问: arr2d[0][2] , arr2d[0, 2]

#三维数组的运用
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
r_1 = arr3d[0][0]
r_2 = arr3d[1][1]
print(r_1)
print(r_2)

print('~~~~~~~~~~~~~~~~~~44444444~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 4.切片索引
#ndarray 的切片语法跟 Python 列表这样的一维对象差不多
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
r_1 = arr[:2] #选取矩阵的前两行
r_2 = arr[2:] #选取矩阵的前两行
print(r_1)
# arr[:2] = 1  #修改视图
print(arr)
print(arr[:2, 1:]) #输出前两行的后两列
print(arr[:2, 1:2]) #输出前两行的中间一列
print(arr[1:3, 2:]) #输出后两行的后两列
print(arr[2:3, :2])  #输出后一行的前两列

#自然，对切片表达式的赋值操作也会被扩散到整个选区

print('~~~~~~~~~~~~~~~~~~55555555~~~~~~~~~~~~~~~~~~~~~~~~~')

#5.布尔型索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)

print(names)
print(data)
print(names == 'Bob')

#布尔型数组的长度必须跟被索引的轴长度一致
#此外，还可以将布尔型数组跟切片、整数（或整数序列，稍后将对此进行详细讲解）混合使用：
t = data[names == 'Bob'] # 此时t为规则  如果布尔型数组的长度不对，布尔型选择就会出错，因此一定要小心。
print(t)
r_1 = data[names == 'Bob', 2:]
r_2 = data[names == 'Bob', 3]
print(r_1)
print(r_2)

#要选择除"Bob"以外的其他值，既可以使用不等于符号（!=），也可以通过~对条件进行否定：
#Python关键字and和or在布尔型数组中无效。要使用&与|。
#mask = (names == 'Bob') | (names == 'Will')
data[data < 0] = 0  #规则
print(data)

#通过一维布尔数组设置整行或列的值也很简单：
data[names != 'Joe'] = 7  #规则
print(data)


print('~~~~~~~~~~~~~~~~~~66666666~~~~~~~~~~~~~~~~~~~~~~~~~')

#花式索引
#花式索引（Fancy indexing）是一个NumPy术语，它指的是利用整数数组进行索引。假设我们有一个8×4数组：
arr = np.empty((8, 4))
print(arr)
for i in range(8):
   arr[i] = i+1
print(arr)

#一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组：
data = np.arange(32).reshape((8, 4))
print(data)
r = data[[1, 5, 7, 2], [0, 3, 1, 2]] #最终选出的是元素(1,0)、(5,3)、(7,1)和(2,2)。无论数组是多少维的，花式索引总是一维的
print(r)
r = data[[1, 5, 7, 2]][:,[0, 3, 1, 2]]
print(r)
# 记住，花式索引跟切片不一样，它总是将数据复制到新数组中,会改变原始数值。

print('~~~~~~~~~~~~~~~~~77777777~~~~~~~~~~~~~~~~~~~~~~~~')

#6.数组转置和轴对换
#转置是重塑的一种特殊形式，它返回的是源数据的视图（不会进行任何复制操作）。数组不仅有transpose方法，还有一个特殊的T属性：
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T) #转置

arr = np.random.randn(6, 3)
r = np.dot(arr.T, arr) #np.dot计算矩阵内积
print(r)

#对于高维数组，transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置（比较费脑子）：
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
arr.transpose((1, 0, 2)) #第一个轴被换成了第二个，第二个轴被换成了第一个，最后一个轴不变
print(arr)

#简单的转置可以使用.T，它其实就是进行轴对换而已。ndarray还有一个swapaxes方法，它需要接受一对轴编号：
arr.swapaxes(1, 2) #swapaxes也是返回源数据的视图（不会进行任何复制操作）
print(arr)
