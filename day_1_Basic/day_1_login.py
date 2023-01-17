#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

count = 0
flag = 1
user_pass = []
lock = []
username = input("username:")

with open(r'.\black_list.txt','r') as f: 
    lock_file = f.readlines()

for i in lock_file:
    line = i.strip('\n')
    lock.append(line)
if username in lock:
    print("user %s has been locked..."%username)
else:
    while count < 3:
        count += 1
        passwd = input("input password:")
        with open(r'.\white_list.txt','r') as f:
            white_file = f.readlines()
        for i in white_file:
            user_pass = i.strip().split()
            if(username == user_pass[0] and passwd == user_pass[1]):
                print("Welcome user {name} login...".format(name=username))
                flag = True
                break
            else:
                continue
        if flag is True:
            break
        else:
            if count == 3:
                print("password input 3 times,user is locked...")
                with open(r'E:\MingData\Python\Days\black_list.txt','a') as lock_file:
                    lock_file.write('%s\n' %username)
                break