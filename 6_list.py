#!/usr/bin/env python3

"""list的用法"""

# list的创建
a = []
print(type(a))
# Python的list内部元素允许不同类型
print([1, 'a', "bb"])
# list的访问，list元素的下标从0开始
a = [1, 2, 3, 4, 5]
print(a[0], a[1], a[2], a[3], a[4])
# list元素从后向前访问
print(a[-1], a[-2], a[-3], a[-4], a[-5])
print(a[0:3])
print(a[:3])
print(a[3:])
