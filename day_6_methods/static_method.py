# static method 静态方法
# 实际上跟类没关系了，可以看作是一个函数，但是必须要类的名字来调用
# 可以理解为把各个不同的功能，打包成了一个类。方便归类管理，

class Dog(object):
    def __init__(self, name) -> None:
        self.name = name

    # def eat(self, food):
    #     print(f"{self.name} is eating {food}")

    # @staticmethod   # 也可以加self, 但是需要把实例自己传进去；实际不这么操作，作用独立开各自的功能
    # def eat(self):
    #     print(f"{self.name} is eating Meat")

    @staticmethod   # 正常的使用
    def eat():
        print(f"Hei is eating Meat")


d = Dog("Ha")
# d.eat("Meat")

# 静态方法的self使用
# d.eat(d)

# 静态方法的常规使用
d.eat()