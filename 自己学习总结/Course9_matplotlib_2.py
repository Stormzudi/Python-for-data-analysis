# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 21:51
# @Author  : Zudy
# @FileName: Course9_matplotlib_2.py
'''
9.1.matplotlib API入门
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
import pandas as pd
from datetime import datetime

inputfile = 'D:/Python/Python_learning/Mach_model/ARIMA_model/data.xlsx' #销量及其他属性数据
data = pd.read_excel(inputfile, index_col = u'时间', parse_dates= True)
spx = data['销量'] #获取series 销量这列


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2015, 1, 7), 'Peak of bull market'),
    (datetime(2015, 1, 21), 'Bear Stearns Fails'),
    (datetime(2015, 2, 1), 'Lehman Bankruptcy')
]

#ax.annotate方法可以在指定的x和y坐标轴绘制标签
#我们使用set_xlim和set_ylim人工设定起始和结束边界
#用ax.set_title添加图标标题
for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor='black', headwidth=4, width=2,
                                headlength=4),
                horizontalalignment='left', verticalalignment='top')

ax.set_xlim(['1/1/2015', '2/6/2015']) #定义x轴的取值范围
ax.set_ylim([2500, 4800]) #定义y轴的取值范围

ax.set_title('Important dates in the 2015/01/01-2015/02/06 financial crisis')
# plt.show()


#要在图表中添加一个图形，你需要创建一个块对象shp，然后通过ax.add_patch(shp)将其添加到subplot中
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color='g', alpha=0.5)

ax.add_patch(rect) #矩形
ax.add_patch(circ) #椭圆
ax.add_patch(pgon) #三角形
plt.show()




print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#9.2 使用pandas和seaborn绘图