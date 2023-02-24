#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import hashlib
import hmac     # 内部对我们创建的key和内容，再加密

# md5
m = hashlib.md5()
m.update(b'Hello')
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())

compare = hashlib.md5()
compare.update(b"HelloIt's me") # 验证前面是不是合并了，而且没有空格。
print(compare.hexdigest())

# sha
s1 = hashlib.sha1()
s1.update(b"HelloIt's me")
print(s1.hexdigest())

s2 = hashlib.sha512()
s2.update("天王盖地虎".encode(encoding='utf-8'))
print(s2.digest())
print(s2.hexdigest())
