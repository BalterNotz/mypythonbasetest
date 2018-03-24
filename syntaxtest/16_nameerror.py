#!/usr/bin/env python3
# Python3

'''
对NameError异常的判断方法：
1 使用type eval方法
2 使用变量命名空间的方法
'''


def isset(v):
    try:
        type(eval(v))
    except:
        return 0
    else:
        return 1

if isset('var_name'):
    print('var_name is defined')
else:
    print('var_name is not defined')

if 'var_name' in locals().keys():
    print('var_name is defined')
else:
    print('var_name is not defined')

