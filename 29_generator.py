# 生成器
'''
在普通类中加入yield即可

yield相当于普通函数中的return语句，只是生成器使用yield时在下一次调用时，
会从上一次返回的地方开始执行。
'''


def myGen():
    print('生成器被执行')
    yield 1
    yield 2


g = myGen()
print(next(g))
print(next(g))


# print(next(g))


def myfibs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield b


for i in myfibs():
    if i < 100:
        print(i, end=' ')
    else:
        break
