# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 20:19
# @Author  : Zudy
# @FileName: Course9_matplotlib_1.py

'''
9.1.matplotlib API入门
    9.1.1 Figure和Subplot
    9.1.2 调整subplot周围的间距
    9.1.3 颜色、标记和线型
    9.1.4 刻度、标签和图例
    9.1.5 设置标题、轴标签、刻度以及刻度标签
    9.1.6 添加图例
    9.1.7 注解以及在Subplot上绘图
    9.1.8 将图表保存到文件
    9.1.9 matplotlib配置
9.2 使用pandas和seaborn绘图
    9.2.1 线型图
    9.2.2 柱状图
    9.2.3 直方图和密度图
    9.2.4 散布图或点图
    9.2.5 分面网格（facet grid）和类型数据
9.3 其它的Python可视化工具
9.4 总结
'''
import matplotlib.pyplot as plt
import numpy as np



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1~~~~~~~~~~~~~~~~~~~~~~')

fig = plt.figure() #创建图例fig
ax = fig.add_subplot(1, 1, 1) #创建画板
data = np.arange(10)
ax.plot(data, label ='one') #设置了一个标签'one'
ax.legend(loc='best') #选取了最好的一个位置
# plt.show()



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.1~~~~~~~~~~~~~~~~~~~~~~')
# 9.1.1 Figure和Subplot
#plt.figure创建一个新的Figure， matplotlib的图像都位于Figure对象中
fig = plt.figure()
#figsize：它用于确保当图片保存到磁盘时具有一定的大小和纵横比。
#不能通过空Figure绘图。必须用add_subplot创建一个或多个subplot才行：

ax1 = fig.add_subplot(2, 2, 1) #图像应该是2×2的（即最多4张图）
ax2 = fig.add_subplot(2, 2, 2)  #fig.add_subplot所返回的对象是AxesSubplot对象
ax3 = fig.add_subplot(2, 2, 3)

# plt.plot(np.random.randn(50).cumsum(), 'k--') #默认存于最后一次建立的图片中
#"k--"是一个线型选项，用于告诉matplotlib绘制黑色虚线图

ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
ax3.plot(np.random.randn(50).cumsum(), 'k--')
# plt.show()



#subplots可以选择相同的y轴或者相同的x轴
fig2, axes = plt.subplots(2, 2, sharex= False, sharey= True)
axes[0,0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
axes[0,1].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
axes[1,0].plot(np.random.randn(50).cumsum(), 'k--')
# plt.show()



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.2~~~~~~~~~~~~~~~~~~~~~~')
#9.1.2 调整subplot周围的间距
#subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)
#wspace和hspace用于控制宽度和高度的百分比

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0) #间距收缩到了0
# plt.show()



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.3~~~~~~~~~~~~~~~~~~~~~~')
#9.1.3 颜色、标记和线型

ax1 = plt.figure() #增加一个画布ax1
x = np.arange(10)
y = np.arange(10)
plt.plot(x, y, 'g--')

ax2 = plt.figure() #增加一个画布ax2
plt.plot(x, y, linestyle='--', color='g')

ax3 = plt.figure()  #增加一个画布ax3
plt.plot(np.random.randn(30).cumsum(), 'ko--')

# plt.show()



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.4 && 9.1.5~~~~~~~~~~~~~~~~~~~~~~')
#刻度、标签和图例
fig = plt.figure() #增加一个画布
ax = fig.add_subplot(1, 1, 1)  #画布的位子为一张图
ax.plot(np.random.randn(1000).cumsum())  #随机漫步

#要改变x轴刻度：set_xticks和set_xticklabels
ticks = ax.set_xticks([0, 250, 500, 750, 1000]) #增加x轴标签刻度（断点）
# labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
# rotation选项设定x刻度标签倾斜30度,


#ax.set_xlabel('x_stages')
#ax.set_title('My first matplotlib plot')
#ax.set_ylabel('y_stages')
#set_xlabel为X轴设置一个名称
props = {
    'title' : 'My first matplotlib plot',
    'xlabel' : 'x_stages',
    'ylabel' : 'y_stages'
}
ax.set(**props)
# plt.show()



print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.6~~~~~~~~~~~~~~~~~~~~~~')
#9.1.6 添加图例
#图例（legend）是另一种用于标识图表元素的重要工具。添加图例的方式有多种。最简单的是在添加subplot的时候传入label参数

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum(), 'k', label= 'one')
ax.plot(np.random.randn(1000).cumsum(), 'k--', label= 'two')
ax.plot(np.random.randn(1000).cumsum(), 'k.', label= 'three')
ax.legend(loc = 'best') #可以调用ax.legend()或plt.legend()来自动创建图例

plt.show()
print('~~~~~~~~~~~~~~~~~~~~~~~~9.1.7~~~~~~~~~~~~~~~~~~~~~~')
