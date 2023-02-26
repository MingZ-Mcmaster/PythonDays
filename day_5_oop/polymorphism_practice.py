"""
polymorphism:多态
为了类在继承和派生的时候，保证使用“家族”中任一类的实例的某一属性时的正确调用
"""

class Animal(object):
    def __init__(self, name) -> None:
        self.name = name

    def talk(self):
        pass

    # 真正的多态
    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Dog(Animal):
    def __init__(self, name) -> None:
        super(Dog, self).__init__(name)

    def talk(self):
        print("Woof Woof")

class Cat(Animal):
    def __init__(self, name) -> None:
        super(Cat, self).__init__(name)

    def talk(self):
        print("Meow, Meow")


#实例化
d = Dog("Ha")
c = Cat("Zha")

# 常规实现
d.talk()
c.talk()

# 多态的一种基础方式，同一个接口，实现不同类的功能
def animal_talk(obj):
    obj.talk()
animal_talk(d)
animal_talk(c)

# 把方法放到父类里去实现
# @staticmethod
# def animal_talk(obj): # no self 也就是不需要实例化
#   obj.talk()
Animal.animal_talk(d)
Animal.animal_talk(c)