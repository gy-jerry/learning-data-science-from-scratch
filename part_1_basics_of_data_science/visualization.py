# coding:utf-8

# 第3章 可视化数据

# print '你好'

from matplotlib import pyplot as plt
from collections import Counter

# settings
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
# 参考：https://segmentfault.com/a/1190000005144275


# '''
# 简单线图
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300, 543, 1075, 2862, 5979, 10289, 14958]

plt.plot(years, gdp, color = 'green', marker='o', linestyle='solid')
plt.title('GDP')
# 使用中文的方法
plt.ylabel(u'十亿')
plt.show()
# '''


# '''
# 条形图
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i for i, _ in enumerate(movies)]
# print (xs)
# xs = [i for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars, width=0.9)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
# plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.xticks([j for j, _ in enumerate(movies)], movies)

plt.show()

# enumerate()函数用法：
# 枚举函数，可以快速遍历列表或者字典，返回的对象中包含了计数和内容
# for index, text in enumerate(movies):
#     print index, text
# 默认从0开始计数，即索引；也可以传入第二个参数，表示从多少开始计数
# print list(enumerate(movies, 2))
# '''


# '''
# 直方图
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# decile = lambda grade: grade // 10 * 10


def decile(grade):
    return grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

# plt.bar([x - 4 for x in histogram.keys()], # shift each bar to the left by 4
plt.bar([x for x in histogram.keys()],
        histogram.values(),                # give each bar its correct height
        8)                                 # give each bar a width of 8
plt.axis([-5, 105, 0, 5])                  # x-axis from -5 to 105,
                                               # y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

# lambda用法：
# 参考上面的代码：
#
# decile = lambda grade: grade // 10 * 10
# def decile(grade):
#     return grade // 10 * 10
#
# 实际上这两种表述是一致的，也就是说，lambda可以定义一个匿名函数decile，不过与def不同的是，lambda可以看做一个表达式
# 当上面情况下，使用lambda定义函数时，pycharm提示PEP8更倾向与使用def
# 因此，lambda更多用于其他表达式内，使代码简洁（其实并不易读，如果不了解Python），特别是单行函数
# 但其实，对于简单匿名函数，有更好的解决方案：for ... in ... if ...
# 举例：实现过滤器，找到列表中的能被3整除的数：
#
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print filter(lambda x: x % 3 == 0, foo)
# print [x for x in foo if x % 3 == 0]
#
# 上面两行输出完全相同，并且即使没接触过Python，for ... in ... if ... 显得更加清晰
#
# 结论：
# lambda可以定义一个匿名函数
# lambda并不会带来程序效率的提高，只会是代码更简洁
# 如果可以使用for ... in ... if ... 来完成的，不要使用lambda
# 如果使用lambda，不要在内部使用循环，如果有，定义函数，获得重用性和更好的可读性
# 参考：http://www.cnblogs.com/evening/archive/2012/03/29/2423554.html
#

# 直方图或柱状图：
# 使用
# plt.axis([-5, 105, 0, 5])
# 指定横纵坐标范围：
# 为把处于边缘的条形显示完全，常将横坐标范围略扩大（上面的例子数据range为0,100）；
# 为了不误导读图，纵坐标常从0开始（一般如此，视情况而定）
# '''


# '''
# 线图
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = range(len(variance))

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,     'g-',  label='variance')     # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')       # red dot-dashed line
plt.plot(xs, total_error,  'b:',  label='total error')  # blue dotted line

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

# zip()函数：
# 接受任意多个list作为参数，将所有list按相同的索引组合成很多tuple，再将这些tuple组合成一个list
# 其中，每个tuple的元素是参数list相同索引的元素
# 同时，新序列的长度与参数list最短的相同
# 另外，操作符 * 与 zip() 函数配合可以实现与 zip() 相反的功能，即将合并的新list拆成多个tuple
#
# 1. 传入list，输出tuple组成的list
#
# x1 = [1, 2, 3]
# y1 = ['a', 'b', 'c']
# print zip(x1, y1)
#
# [(1, 'a'), (2, 'b'), (3, 'c')]
#
# 2. list的长度与参数中最短的list一致
#
# x1 = [1, 2, 3]
# y1 = ['a', 'b']
# print zip(x1, y1)
#
# [(1, 'a'), (2, 'b')]
#
# 3. 操作符 * 及其用法
#
# x1 = [1, 2, 3]
# y1 = ['a', 'b', 'c']
# print zip(*zip(x1, y1))
#
# [(1, 2, 3), ('a', 'b', 'c')]
#
# '''


# '''
# 散点图
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),  # put the label with its point
                 xytext=(5, 0),  # but slightly offset 避免标记与点重合
                 textcoords='offset points')

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

for equal_axes in [False, True]:
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")

    if equal_axes:
        plt.title("Axes Are Comparable")
        # 绘制散点图，当两个坐标轴表示的实际意义相关，需要使两个坐标轴尺度一致
        plt.axis("equal")
    else:
        plt.title("Axes Aren't Comparable")

    plt.show()
# '''
