__author__ = "Ming"

"""
1. 面向对象：类，class
2. 面向过程：def, 有返回值
3. 函数式编程：def, 无返回值, 一般是隐式返回None

    返回值：
        无返回值：None
        有一个返回值：object
        有多个返回值：tupple
"""
import time

def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('function_test.txt', 'a+') as f:
        f.write(f'{time_current} end action\n')

def test1():
    print("in the test 1")
    logger()

def test2():
    print("in the test 1")
    logger()

def test3():
    print("in the test 1")
    logger()

test1()
test2()
test3()

def test(*args):    # tuple
    print(args, type(args))

def test_kw(**kwargs):  # dict
    print(kwargs, type(kwargs))

test(1,2,3,4,5,6, [1,2,3,4,5,6])
test_kw(name='Ming', age=38)