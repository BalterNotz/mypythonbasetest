# 魔法方法
# 构造析构

# __new__ 可用于不可变对象实例化过程中的一些操作
class CapStr(str):
    def __new__(cls, *args, **kwargs):
        string = ''
        for s in args:
            print(s)
            string = string + str(s).upper()
        return super().__new__(cls, string)

    def __del__(self):
        print('调用析构函数，垃圾回收的时候调用。')


cs = CapStr('asdfasdf', 'jkljkljkl')
print(cs)


# __init__


# __del__ 垃圾回收的时候才会调用该方法，执行 del 删除对象并不一定会执行__del__方法


# 重写魔法方法，可以实现自定义的操作
class NewInt(int):
    def __add__(self, other):
        return int.__sub__(self, other)

    def __sub__(self, other):
        return int.__add__(self, other)


a = NewInt(2)
b = NewInt(3)
print(a + b)
print(a - b)


# Python中的反运算，指当左边的对象不支持当前操作时，由右过的对象进行调用
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)


a = Nint(5)
b = Nint(3)
print(a + b)
print(1 + b) # 1 不支持 + 操作，由右边的b调用反远算


#魔法方法还可以用来实现自定义的容器，迭代器等