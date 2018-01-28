#!/usr/bin/env python3
# Python3

'''继承的用法'''


class MyList(list):
    pass


myl = MyList()
myl.append(3)
myl.append(5)
myl.append(4)

myl.sort()
print(myl)

myl2 = MyList()
myl2.extend({1, 3, 2})
myl2.sort()
print(myl2)


# 子类如果定义了和父类相同的函数，则需要先调用父类的同名函数。

class Fish:
    def __init__(self):
        self.x = 5


class GoldFish(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.y = 3


class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.y = 33


class SShark(Fish):
    def __init__(self):
        self.y = 3333
        super().__init__()


class Animal:
    def __init__(self):
        self.z = 2


# 多继承，注意init方法中调用的父类方法。
class Frog(Fish, Animal):
    def __init__(self):
        Fish.__init__(self)
        Animal.__init__(self)
        pass


f = Fish()
print(f.x)
gf = GoldFish()
print(gf.x, gf.y)
s = Shark()
print(s.x, s.y)
ss = SShark()
print(ss.x, ss.y)

frog = Frog()
print(frog.x, frog.z)
