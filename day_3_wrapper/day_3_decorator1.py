#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Ming"

import time
import os
os.system('')

user, password = 'ming', 'abc'
# 6. 因为增加了需求，传进去的参数也要有所调整，需要和外部一致，也就是说auth(func)变成了auth(auth_type)
# 2. 因为需求，增加了验证身份的装饰器
def auth(auth_type):
    # 6. 为了适应验证的不同，需要增加一层wrapper，也就是增加了这个wrapper的深度
    
    def outer_wrapper(func):
        print("auth func", auth_type)    # for tracking
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)    # for tracking
            # 7. 增加auth条件的判断
            if auth_type == "local":
                username = input("Username:").strip()
                pswd = input("Password:").strip()

                if username == user and pswd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    # 5. 为了适应4的返回值，需要调整func(*args, **kwargs)，为其赋值
                    # func(*args, **kwargs)
                    res = func(*args, **kwargs)
                    print("----Authentication is Done----")
                    return res
                else:
                    exit("\033[31;1mInvalide authentication\033[0m")
            elif auth_type == "ldap":
                print("No Server right now")
                
        return wrapper
    return outer_wrapper

# 6. 根据需求，增加了本地验证和LDAP服务器验证，所以对装饰器增加了要求
# 3. 需要增加登录验证了，所以增加一个auth装饰器

# 1. 初始化网站页面
def index():
    print("Welcomd to index page")

@auth(auth_type = "local")
def home():
    print("Welcome to home page")
    # 4. 增加了返回值，但是2 wrapper 还没有调整，所以不会有返回值
    return "from home"

@auth(auth_type = "ldap")
def bbs():
    print("Welcomd to bbs page")

index()
# 5. 由于func有了返回值，所以需要打印其返回值，故注释掉，而改为print(home())
# home()
print(home())
bbs()
