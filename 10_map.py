#!/usr/bin/env python3
# Python3

l = [1,2,3,4,5]
f = lambda x : x * 2

if __name__ == '__main__':
    print(list(map(f,l)))