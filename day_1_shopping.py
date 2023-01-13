#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import os
os.system('')

product_list = [
    ('P16G1',3100),
    ('i9-12900HX',600),
    ('RTX-A5500',1000),
    ('Electronic Car',40000),
    ('Coffee',9.99),
    ('Desk Top',5000),
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    # print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary) )
                    print(f"Added {p_item} into shopping cart,your current balance is \033[31;1m{salary}\033[0m" )
                else:
                    # print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
                    print(f"\033[41;1m你的余额只剩{salary}啦，还买个毛线\033[0m")
            else:
                print("product code [%s] is not exist!"% user_choice)
        elif user_choice == 'q':
            if len(shopping_list) == 0:
                print("You cart is empty. Thank you for using this system.")
                exit()
            print("--------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("invalid option")
else:
    print("Invalid salary value")