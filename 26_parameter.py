# 参数的用法

def abc(a, b=3, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


# abc()
abc(1)
print('第二次测试')
abc(1, 2, 3, 4, 5)
print('第三次测试')
abc(1, 2, 3, 4, 5, {'abc': 'def'})

print('测试defunc函数') #注意后面的赋值参数转换成了字典
abc(1, 2, 3, 4, 5, abc = 'def', jkl = 'asdfasdf')
abc(1, 2, 3, abc = 'def', jkl = 'asdfasdf')
