#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import os
import getpass
os.system('')

_user_name = "Ming"
_password = "abc123"

user_name = input("username: ")
password = getpass.getpass("password: ")

if _user_name == user_name and _password == password:
    print("Welcome user {name} login..." .format(name=user_name))
else:
    print("\033[33;41m Invalid Username or Password \033[0m")