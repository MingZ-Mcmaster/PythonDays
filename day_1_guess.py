#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
title: 猜年龄
猜3次
    3次内返回hint;
    3次外询问是否继续
        如果继续, 重新3次
否则结束
"""
age = 38
count = 0

while count < 3:    # 进入循环
    count += 1      # 自动+1
    print("Count: ", count)
    
    guess_age = int(input("Guess age: "))
    if guess_age == age:    # 猜对了
        print("Bingo! You guess {_count} times".format(_count=count))
        break
    elif guess_age > age:   # 猜大了
        print("Think smaller")
    else:                   # 猜小了
        print("Think bigger")
    if count == 3:          # 达到3次了
        continue_confirm = input("Do you want to keep guessing? [y/n]")
        if continue_confirm != 'n': # 继续
            count = 0
else:                       # 结束
    print("Too many times... fuck off")