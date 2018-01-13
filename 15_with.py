#!/usr/bin/env python3
# Python3

'''with语句：
with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，
释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
'''

import random

filename = str(random.randint(10000000000, 100000000000))
print('filename = %s' % filename)
# 没有使用with
try:
    f = open(filename)
    print('文件已经被打开')
except OSError as e:
    print('异常啦：%s' % e)
finally:
    try:
        f.close()
    except:
        pass

#使用with
try:
    with open(filename) as f:
        print('文件已经被打开')
except OSError as e:
    print('异常啦：%s' % e)