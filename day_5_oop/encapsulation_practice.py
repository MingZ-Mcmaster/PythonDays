#!/usr/bin/env python3

class Dog:
    """
    Encapsulation封装
    使得代码模块化
    """
    def __init__(self, name):
        self.name = name
    
    def bulk(self):
        print(f"{self.name}: wang wang wang")

d1 = Dog("A")
d1.bulk()
d2 = Dog("B")
d2.bulk()