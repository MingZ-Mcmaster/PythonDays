# 类方法
# 只能访问类变量，不能访问实例变量

class Dog(object):
    name = "Hei"
    def __init__(self, name) -> None:
        self.name = name

    # def eat(self, food):
    #     print(f"{self.name} is eating {food}")

    @classmethod  # 不管怎么调用，也只能访问类变量，而不能访问实例变量
    def eat(self):
        print(f"{self.name} is eating Meat")


d = Dog("Ha")
d.eat() 