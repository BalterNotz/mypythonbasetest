#!/usr/bin/env python3
# Python3

'''
类定义--》类对象--》实例对象
类对象是静态的，与C语言中的static相似
属性和方法如果同名，则后定义的覆盖先定义的。

什么是绑定（bind）


对象的定义:
self是什么？self代表类的实例，是一个形参名，不必非得是self这个名字。
Python解释器在调用函数时是这样子调用的：ClassName.Func(self...)如：
class Classname:
    def prt(self):
        print(self)

obj = Classname()
obj.prt()这个调用在Python解释器解释的时候是这样子执行的：
Classname.prt(obj...)

如果在定义的时候不定义self，那么该方法就变为了类方法，不能由类的实例
进行调用，只能由类进行调用，如下：
class Classname:
    def prt():
        print(__class__)
obj = Classname()
obj.prt()这样子调用会报错，定义少参数，只能使用类进行调用，如：
Classname.prt()


Python的魔法方法：以__（双下划线）开始和结尾
__init__(self)


公有与私有：
默认为公有的，若需要定义私有的属性或方法，只需要有名字前加__(双下划线)
但Python实现私有的方法是将属性或方法的名字进行重命名的方法来实现的，如：
原有名字是__name，如若需要访问可以通过
obj._Classname__name进行访问。
'''


class Turtle:
    # 属性
    color = 'green'
    __age = 28

    # 方法
    def climb(self):
        print('''I'm climbing''')

    def getAge(self):
        return self.__age


if __name__ == '__main__':
    t = Turtle()
    t.climb()
    t.name = 'abc'
    print(t.name)
    print(t.getAge())
    print(t._Turtle__age) #通过命名重整访问私有属性
