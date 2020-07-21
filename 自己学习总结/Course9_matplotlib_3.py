# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 18:36
# @Author  : Zudy
# @FileName: Course9_matplotlib_3.py

'''
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
import pandas as pd
import seaborn as sns

# print('~~~~~~~~~~~~~~~~~~ 9.2.1 线型图~~~~~~~~~~~~~~~~~~')
# #你组装一些基本组件就行：
# # 数据展示（即图表类型：线型图、柱状图、盒形图、散布图、等值线图等）、图例、标题、刻度标签以及其他注解型信息。
#
# #使用dataframe 和 serise 中的数据画图
# s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
#
# #X轴的刻度和界限可以通过xticks和xlim选项进行调节，Y轴就用yticks和ylim
# # s.plot(xlim = [0,100], ylim = [-5,5]) #x,y的 取值范围
# s.plot()
# plt.show()
#
#
# # ax参数 使你能够在网格布局中更为灵活地处理subplot的位置
# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
#                   columns= ['A', 'B', 'C', 'D'],
#                   index= np.arange(0, 100, 10))
# df.plot()
# plt.show()
#
#
# print('~~~~~~~~~~~~~~~~~~ 9.2.2 柱状图~~~~~~~~~~~~~~~~~~')
# #DataFrame还有一些用于对列进行灵活处理的选项，
# # 例如，是要将所有列都绘制到一个subplot中还是创建各自的subplot
# fig, axes = plt.subplots(2, 1)
# data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
# data.plot.bar(ax = axes[0], color = 'k', alpha = 0.7)
# data.plot.barh(ax = axes[1], color = 'k', alpha = 0.7)
# #color='k'和alpha=0.7设定了图形的颜色为黑色，并使用部分的填充透明度
# plt.show()
#
#
# #对于DataFrame，柱状图会将每一行的值分为一组，并排显示
# df = pd.DataFrame(np.random.rand(6, 4),
#                   index=['one', 'two', 'three', 'four', 'five', 'six'],
#                   columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus')
#                   )
# df.plot.bar() #返回每行的bar()
# df.plot.barh(stacked=True, alpha=0.5) #设置stacked=True即可为DataFrame生成堆积柱状图
# plt.show()
#
# #做一张堆积柱状图以展示每天各种聚会规模的数据点的百分比
# tips = pd.read_csv('D:/Python/Python_learning/Python_The_data_analysis/tips.csv')
# party_counts = pd.crosstab(tips['day'], tips['size']) #根据日期和聚会规模创建一张交叉表
# print(party_counts)
# party_counts = party_counts.loc[:, 2:5]
# party_pcts = party_counts.div(party_counts.sum(1), axis=0) #规格化，使得各行的和为1
# print(party_pcts)
# party_pcts.plot.bar() #画出每天各种聚会规模的比例
# plt.show()
#
#
# #用seaborn来看每天的小费比例
# tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
# print(tips.head())
# sns.barplot(x='tip_pct', y='day', data=tips, orient='h') # 小费的每日比例，带有误差条
# #seaborn的绘制函数使用data参数，它可能是pandas的DataFrame
# plt.show()
#
#
#
# print('~~~~~~~~~~~~~~~~~~ 9.2.3 直方图和密度图~~~~~~~~~~~~~~~~~~')
# # 画出小费占消费总额百分比tips['tip_pct']的直方图
# tips['tip_pct'].plot.hist(bins=50) #小费百分比的直方图
# tips['tip_pct'].plot.density()
# plt.show()
#
# #考虑一个双峰分布，由两个不同的标准正态分布组成
# comp1 = np.random.normal(0, 1, size =200)
# comp2 = np.random.normal(10, 2, size =200)
# values = pd.Series(np.concatenate([comp1, comp2])) #标准混合密度估计的标准直方图
# sns.distplot(values, bins=100, color='k')
# plt.show()


print('~~~~~~~~~~~~~~~~~~ 9.2.4 散布图或点图~~~~~~~~~~~~~~~~~~')
macro = pd.read_csv('macrodata.csv')


data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
# data = macro[['m1', 'unemp']]
trans_data = np.log(data).diff().dropna() #计算对数差
print(trans_data[5:])

#然后可以使用seaborn的regplot方法，它可以做一个散布图，并加上一条线性回归的线
sns.regplot('m1', 'unemp', data = trans_data) # seaborn的回归/散布图
plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))
plt.show()

#statsmodels macro data的散布图矩阵
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
plt.show()


print('~~~~~~~~~~~~~~~~~~ 9.2.5 分面网格（facet grid）和类型数据~~~~~~~~~~~~~~~~~~')
#seaborn有一个有用的内置函数factorplot，可以简化制作多种分面图
tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
print(tips)

#按照天/时间/吸烟者的小费百分比
sns.factorplot(x='day', y='tip_pct',
               hue='time',
               col='smoker',
               kind='bar',
               data= tips[tips.tip_pct < 1])
# 按天的tip_pct，通过time/smoker分面
sns.factorplot(x='day', y='tip_pct', row='time',
               col='smoker',
               kind='bar',
               data=tips[tips.tip_pct < 1])
#按天的tip_pct的盒图
sns.factorplot(x='tip_pct', y='day',
               kind='box',
               data=tips[tips.tip_pct < 0.5])
plt.show()



