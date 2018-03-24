#!/usr/bin/env python3
# Python3

'''pickle模块用于将对象转换成二进制格式，可以保存在文件中'''

import pickle
import os

l = list(range(1, 10))

f = open('./bindata.pkl', 'wb')
pickle.dump(l, f)
f.close()
f = open('./bindata.pkl', 'rb')
l = pickle.load(f)
f.close()
print(l)
print(list(l))
