# -*- coding:utf-8 -*-
"""
                UNICODE
    ||                      ||
    utf-8                   GBK
"""

import sys
print(sys.getdefaultencoding())

# 字符串，可以
s = "你好"  # 两个汉字
print(s, type(s))

# encode成byte，默认是utf-8
s_byte = s.encode()     # 每个汉字3个字节
print("转成Byte: ", s_byte)

# 解码成字符串
s_to_utf = s_byte.decode('utf-8')
print("解析成utf-8: ", s_to_utf, type(s_to_utf))

# encode成byte with GBK
s_to_gbk = s.encode("gbk")  # 每个汉字2个字节
print("解析成gbk: ", s_to_gbk, type(s_to_gbk))