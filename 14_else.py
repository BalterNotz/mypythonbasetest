#!/usr/bin/env python3
# Python3

'''else 的用法：
1 三元表达式
2 if else语句
3 与Exception一起使用，当没有异常发生时执行
4 与循环一起使用，当循环完成时执行（没有被break中途中断）
'''
# 三元表达式
a = 1
b = 2
x = a if True else b
y = a if False else b
print('x = %d' % x)
print('y = %d' % y)

# if else
if a > b:
    print('a > b')
else:
    print('a < b')

# 与循环一起，只有在循环完成之后执行
for i in range(1, 3):
    print(i)
else:
    print('for循环已完成')
# 循环没有完成不会执行后面的else语句
for i in range(1, 3):
    break
else:
    print('for循环已完成')
i = 10
while i in range(1, 3):
    print(i)
    i = i + 1
else:
    print('while循环已完成')
i = 1
while i in range(1, 3):
    print(i)
    i = i + 1
else:
    print('while循环已完成')

# 下面这个while循环被break了，后面的else语句不会执行
i = 1
while i in range(1, 3):
    print(i)
    i = i + 1
    if i == 2:
        break
else:
    print('while循环已完成')

# Exception一起使用，当没有异常发生时执行
try:
    print('没有异常')
except Exception:
    print('有异常发生')
else:
    print('有异常发生时不会执行else')
try:
    print('有异常')
    raise Exception('异常啦')
except Exception as e:
    print('有异常发生: %s' % e)
else:
    print('有异常发生时不会执行else')