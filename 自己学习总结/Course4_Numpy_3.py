# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 21:16
# @Author  : ZhuNian
# @FileName: Numpy_3.py
# @Software: PyCharm
'''
Numpy有关知识
4.4 用于数组的文件输入输出
4.5 线性代数
4.6 伪随机数生成
4.7 示例：随机漫步
    4.7.1.一次模拟多个随机漫步
4.8 结论
'''

import numpy as np
import random
import matplotlib.pyplot as plt

print('~~~~~~~~~~~~~~~~~~~~~4.4~~~~~~~~~~~~~~~~~~~~')
#4.4 用于数组的文件输入输出
arr = np.arange(10)
np.save('some_array', arr)
t = np.load('some_array.npy')
print(t)

#通过np.savez可以将多个数组保存到一个未压缩文件中，将数组以关键字参数的形式传入即可：
np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])
print(arch['a'])



print('~~~~~~~~~~~~~~~~~~~~~4.5~~~~~~~~~~~~~~~~~~~~')
#4.5 线性代数
x = np.array([[1., 2., 3.], [4., 5., 6.]])
t = np.ones(3)
r = np.dot(x, t.T)  #r = np.dot(x, t)也行
print(t)
print(r)

print('~~~~~~~~~~~~~~~~~~~~~4.6~~~~~~~~~~~~~~~~~~~~')
#4.6 伪随机数生成
#numpy.random模块对Python内置的random进行了补充，增加了一些用于高效生成多种概率分布的样本值的函数。
samples = np.random.normal(size=(4, 4))
print(samples)
r = np.random.seed(1234)
print(r)


print('~~~~~~~~~~~~~~~~~~~~~4.7~~~~~~~~~~~~~~~~~~~~')
#4.7 示例：随机漫步
#先来看一个简单的随机漫步的例子：从0开始，步长1和－1出现的概率相等
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
# plt.show()

#不难看出，这其实就是随机漫步中各步的累计和，可以用一个数组运算来实现。
#因此，我用np.random模块一次性随机产生1000个“掷硬币”结果（即两个数中任选一个），
#将其分别设置为1或－1，然后计算累计和：
nsteps = 1000
draws = np.random.randint(0, 2, size= nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
print(walk) #累加
print(walk.min())
print(walk.max())
plt.plot(walk[:100])  #运用np.random.randint产生随机数
plt.show()
r = (walk == 2).argmax() #找到第一个等于2的位置
print(r)


print('~~~~~~~~~~~~~~~~~~~~~4.7.1~~~~~~~~~~~~~~~~~~~~')

#一次模拟多个随机漫步
#numpy.random的函数传入一个二元元组就可以产生一个二维数组
nsteps = 1000
nwalks = 5000
draws = np.random.randint(0, 2, size= (nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
r_1 = walks.max()
r_2 = walks.min()
print(r_1,r_2)


#我们来计算30或－30的最小穿越时间
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum()) # Number that hit 30 or -30

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1) #调用argmax在轴1上获取（第一次满足条件的 walks[hits30]) >= 30）穿越时间：
print(crossing_times)
print(crossing_times.mean())
steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
print(steps)


