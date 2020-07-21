# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 16:50
# @Author  : ZhuNian
# @FileName: Numpy_2.py
# @Software: PyCharm

'''
Numpy有关知识
4.2 通用函数：快速的元素级数组函数
4.3 利用数组进行数据处理
    4.3.1 将条件逻辑表述为数组运算
    4.3.2 数学和统计方法
    4.3.3 用于布尔型数组的方法
    4.3.4 排序
    4.3.5 唯一化以及其它的集合逻辑
4.4 用于数组的文件输入输出
4.5 线性代数
4.6 伪随机数生成
4.7 示例：随机漫步
    4.7.1.一次模拟多个随机漫步
4.8 结论
'''
import numpy as np
import matplotlib.pyplot as plt

print('~~~~~~~~~~~~~~~~~~~~4.2~~~~~~~~~~~~~~~~~~~~~')
# 4.2 通用函数：快速的元素级数组函数
#通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数
#你可以将其看做简单函数（接受一个或多个标量值，并产生一个或多个标量值）的矢量化包装器
arr = np.arange(10)
#许多ufunc都是简单的元素级变体，如sqrt和exp
r_1 = np.sqrt(arr)
r_2 = np.exp(arr)
print(r_1)
print(r_2)

#这些都是一元（unary）ufunc。另外一些（如add或maximum）接受2个数组（因此也叫二元（binary）ufunc），并返回一个结果数组：
x = np.arange(1,6,dtype=None)
y = np.arange(2,7,dtype=None)

r_1 = np.maximum(x, y) #numpy.maximum计算了x和y中元素级别最大的元素
r_2 = np.add(x, y) #numpy.maximum计算了x和y中元素级别对应值相加
print(x)
print(y)
print(r_1)
print(r_2)

#虽然并不常见，但有些ufunc的确可以返回多个数组。modf就是一个例子，
#它是Python内置函数divmod的矢量化版本，它会返回浮点数数组的小数和整数部分：
remainder, whole_part = np.modf(arr) #将数组的小数和整数返回
print(remainder)
print(whole_part)


print('~~~~~~~~~~~~~~~~~~~~4.3~~~~~~~~~~~~~~~~~~~~~')
#4.3 利用数组进行数据处理
points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
xs, ys = np.meshgrid(points, points)
print(points)
print(len(xs))  #1000*1000 的矩阵
print(xs)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

#作为第9章的先导，我用matplotlib创建了这个二维数组的可视化
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show() #展现图片

print('~~~~~~~~~~~~~~~~~~~~4.3.1~~~~~~~~~~~~~~~~~~~~~')
#4.3.1 将条件逻辑表述为数组运算
#numpy.where函数是三元表达式x if condition else y的矢量化版本
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result,type(result))

#若使用np.where，则可以将该功能写得非常简洁
result = np.where(cond, xarr, yarr) #np.where的第二个和第三个参数不必是数组，它们都可以是标量值。
print(result,type(result))
#假设有一个由随机数据组成的矩阵，你希望将所有大于0.5替换为2，将所有小于0.5替换为－2
arr = np.random.rand(4, 4)
r = arr > 0.5
r_1 = np.where(r, 2, -2)
print(r)
print(r_1)
#可以将标量和数组结合起来
r = np.where(arr > 0.5, 2, arr) # set only positive values to 2
print(r)

print('~~~~~~~~~~~~~~~~~~~~4.3.2~~~~~~~~~~~~~~~~~~~~~')

#数学和统计方法
#可以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算
#sum、mean以及标准差std等聚合计算（aggregation，通常叫做约简（reduction））
# 既可以当做数组的实例方法调用，也可以当做顶级NumPy函数使用。
arr = np.arange(12).reshape(3,4)
r_1 = arr.mean()
# r_1 = arr.mean(arr)
r_2 = arr.sum()
r_3 = arr.mean(axis = 1) #表示计算每行的平均值
r_4 = arr.sum(axis = 0) #表示计算每列的和
print(arr)
print(r_1)
print(r_2)
print(r_3)
print(r_4)

#其他如cumsum和cumprod之类的方法则不聚合，而是产生一个由中间结果组成的数组：
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
r_1 = arr.cumsum()
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
r_2 = arr.cumsum(axis=0) #所有元素累计和
r_3 = arr.cumprod(axis=1) #所有元素的累计积
print(r_1)
print(arr)
print(r_2)
print(r_3)

print('~~~~~~~~~~~~~~~~~~~~4.3.3~~~~~~~~~~~~~~~~~~~~~')
arr = np.random.randn(100)
r = (arr > 0).sum()  # Number of positive values
print(r)
#另外还有两个方法any和all，它们对布尔型数组非常有用
bools = np.array([False, False, True, False])
print(bools.any()) #any用于测试数组中是否存在一个或多个True
print(bools.all()) #而all则检查数组中所有值是否都是True

print('~~~~~~~~~~~~~~~~~~~~4.3.4~~~~~~~~~~~~~~~~~~~~~')
#跟Python内置的列表类型一样，NumPy数组也可以通过sort方法就地排序
arr = np.random.randn(6)
print(arr)
r = arr.sort() #操作视图 原始数据也会改变
print(arr)

#多维数组可以在任何一个轴向上进行排序，只需将轴编号传给sort即可：
arr = np.random.randn(5, 3)
print(arr)
arr.sort(0) #按列排序
#arr.sort(1) 按行排序
print(arr)

print('~~~~~~~~~~~~~~~~~~~~4.3.5~~~~~~~~~~~~~~~~~~~~~')
#唯一化以及其它的集合逻辑
#NumPy提供了一些针对一维ndarray的基本集合运算。最常用的可能要数np.unique了，它用于找出数组中的唯一值并返回已排序的结果：
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))
print(sorted(set(names))) #纯Python代码

#另一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格，返回一个布尔型数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
r = np.in1d(values, [2, 3, 6])
print(r)

