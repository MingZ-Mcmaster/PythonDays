#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Ming"

# 装饰器： 
#   定义: 本质是函数，（装饰其它函数）就是为其他函数添加附加功能。
#   原则:   1. 不能修改被装饰的函数的源代码
#           2. 不能修改被装饰的函数的调用方式（对使用者来说是透明的，他不知道装饰器的存在或者做了什么）

# 实现装饰器：
#   1. 函数即“变量”
#   2. 高阶函数
#       a. 把一个函数名当做实参传给另一个函数 (在不修改被装饰函数源代码的情况下为其添加功能)
#       b. 返回值中包含函数名 （不修改函数的调用方式）
#   3. 嵌套函数
#   高阶函数 + 嵌套函数 =》 装饰器

import time

def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("The func run time is %s" %(stop_time-start_time))
    return wrapper

@timmer     # test1 = timmer(test1)
def test1():
    time.sleep(1)
    print("Test 1: ")

def test2():
    time.sleep(1)
    print("Test 2: ")

@timmer
def test3():
    time.sleep(1)
    print("Test 3")

test1()
test2()
test3()