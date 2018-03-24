#!/usr/bin/env python3
# Python3

'''多态'''


class A():
    def fun(self):
        print('aaa')


A().fun()


class B(A):
    pass


B().fun()


class C(A):
    def fun(self):
        print('ccc')


C().fun()
