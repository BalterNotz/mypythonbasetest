'''
描述符是某种特殊类型的实例，用于指派给另一个类的属性
需要实现以下魔法方法
__get__(self, instance, owner)
__set__(self, instance, owner)
__delete(self, instance)
'''


class MyProperty():
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class C:
    def __init__(self):
        self._x = None
        self.__y = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)


c = C()
c.x = 'X-man'
print(c.x)
print(c._x)
#print(c.__y)
