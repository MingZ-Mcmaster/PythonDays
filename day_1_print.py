# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Author: Ming

name = input("Name: ")
age = int(input("Age: "))
salary = float(input("Salary: "))

# Method 1
info = """
---- info of %s ----
Name: %s
Age: %d
Salary: %f
"""%(name, name, age, salary)

print(info)

# Method 2
info2 = """
---- info of {_name} ----
Name: {_name}
Age: {_age}
Salary: {_salary}
""" .format(_name=name, _age=age, _salary=salary)

print(info2)

# Method 3
info3 = """
---- info of {0} ----
Name: {0}
Age: {1}
Salary: {2}
""" .format(name, age, salary)

print(info3)

# Method 4
info4 = f"""
---- info of {name} ----
Name: {name}
Age: {age}
Salary: {salary}
""" 

print(info4)