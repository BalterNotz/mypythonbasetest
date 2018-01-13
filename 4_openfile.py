#!/usr/bin/env python3

"""use file"""

file = open("text.txt")
line = file.readline()
while line:
    print(line, end="\r\n")
    line = file.readline()
file.close()


"""Python 不支持do while语法，要用break语法模拟"""

file = open("text.txt")
while True:
    line = file.readline()
    if line:
        print(line, end="\r\n")
    else:
        break
file.close()

