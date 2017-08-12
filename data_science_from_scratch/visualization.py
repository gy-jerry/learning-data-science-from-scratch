#coding:utf-8

# 第3章 可视化数据

# print '你好'

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 线图
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300, 543, 1075, 2862, 5979, 10289, 14958]

plt.plot(years, gdp, color = 'green', marker='o', linestyle='solid')
plt.title('GDP')
# 使用中文的方法
plt.ylabel(u'十亿')
plt.show()


# 条形图
