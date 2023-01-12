#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os, sys

# string --> byte (encode); string <-- byte (decode)
msg = "我爱北京天安门! I love China!"
print("String: ", msg)
print("Encoding: ", msg.encode("utf-8"))
print("Decoding: ", msg.encode("utf-8").decode("utf-8"))

#把用户的输入的参数当作一条命令交给os.system来执行
"""
python day_1_modules.py dir
  运行dir
"""
os.system(''.join(sys.argv[1:])) 

# 命令执行语句，但不能保存
os.system("dir")  # 命令直接调用，输出在屏幕上，不会保存，返回执行成功(0)

# 命令执行语句，保存方法
   # cmd_res会保存命令执行的地址
cmd_res = os.popen("dir")
print(cmd_res)                   
  # 需要用read()取回结果
cmd_res = os.popen("dir").read()
print(cmd_res)

# 路径打印语句
print(sys.path) # 打印一个路径的列表：包含所有用过的库、文件的路径
print(len(sys.path))

# 打印输入的参数
"""
python day_1_sys.py hello world --> 
  打印'.\\ day_1_sys.py', 'hello', 'world'
  打印出一个list，里面有三个参数
"""
print(sys.argv)
print(len(sys.argv))

# 顺序输出0到4
for i in range(5):
    print("loop", i)    # print 0 1 2 3 4

# 输出0 2 4 6 8
for i in range(0, 10 ,2):
    print("loop", i)    # print 0 2 4 6 8

# Joint account (浅copy)
import copy # copy.copy(file_name)

person = ['name', ['checking', 1000], ['saving', 20000]]
person_1 = person[:]
person_2 = person[:]

person_1[0] = 'Ming'
person_2[0] = 'Yang'

print(person_1, '\n', person_2)
person_1[1][1] = 888
print(person_1, '\n', person_2)