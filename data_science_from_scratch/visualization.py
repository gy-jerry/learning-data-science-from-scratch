# 中文编码
# coding:utf-8

# 第3章 可视化数据

# print '你好'

from matplotlib import pyplot as plt

# settings
# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False


# 线图
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300, 543, 1075, 2862, 5979, 10289, 14958]

plt.plot(years, gdp, color = 'green', marker='o', linestyle='solid')
plt.title('GDP')
# 使用中文的方法
plt.ylabel(u'十亿')
plt.show()


# 条形图
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()