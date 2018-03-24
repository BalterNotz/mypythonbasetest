#内置函数（BIF）

#一个类会被认为是自己的子类
issubclass(class, classinfo)

#检查一个对象是否是一个类的实例
isinstance(object, classinfo)

#检查对象是否有一个属性
hasattr(object, name)

#取得指定的属性值，如果指定的属性不存在返回默认值
getattr(object, name[, default])

#设置对象的属性值
setattr(object, name, value)

#通过属性设置属性，有点像Http的RESTful接口，将调用转化为资源进行访问
property(fget = None, fset = None, fdel = None, doc = None)