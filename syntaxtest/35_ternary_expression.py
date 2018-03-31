#!/usr/bin/env python
# Python3

a = 1
b = 2
c = a if a > b else b
print(c)
c = 0
c = [a, b][a > b]
print(c)
c = 0
c = [b, a][a > b]
print(c)

# 解释一下[b,a][a>b]的原理，a>b返回bool类型数据，
# 转换成list的索引0，1从列表中取值，但性能怎样？
