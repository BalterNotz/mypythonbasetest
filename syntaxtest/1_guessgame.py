#!/usr/bin/env python3
# Python3

import random

secret = random.randint(0, 10)
print("非常欢迎玩猜数字游戏\n请输入你猜测的数字: ")
guess = int(input())
while guess != secret:
    if guess < secret:
        print("猜小了！")
    else:
        print("猜大了！")
    print("请输入您猜测的数字：")
    guess = int(input())
print("恭喜猜对了！")
