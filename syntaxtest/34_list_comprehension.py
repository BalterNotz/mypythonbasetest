#!/usr/bin/env python
# Python3

l_1 = [p for p in range(10)]
print(l_1)
l_1 = [str(p) for p in range(10)]
print(l_1)
[a, b, c, d] = [i for i in range(4)]
print(a, b, c, d)

l = [i + j for i in range(4) for j in range(4)]
print(l)
l = [(i, j) for i in range(4) for j in range(4)]
print(l)
l = [i for i in range(10) if i % 2 == 0]
print(l)
l = [i for i in range(10) if i % 2 is 0]
print(l)
l = (i for i in range(3))
print(type(l))
for i in range(6):
    print(i, next(l))

