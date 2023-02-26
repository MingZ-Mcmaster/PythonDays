# 属性方法
# 把一个方法变成一个静态属性，隐藏了实现的细节
# 变属性后，不能传参，所以需要增加新的传参函数@eat.setter
# 并在初始化时，设置一个参数，方便静态属性执行的时候直接运行

class Dog(object):
    def __init__(self, name) -> None:
        self.name = name
        self.__food = None

    # def eat(self, food):
    #     print(f"{self.name} is eating {food}")

    @property  # 因为把一个方法变成了一个静态属性了，所以调用时，就不能加（）了，所以也不能传参数了
    def eat(self):
        print(f"{self.name} is eating {self.__food}")

    @eat.setter # 给属性方法赋值
    def eat(self, food):
        print(f"Set to food: {food}")
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("Deleted")


d = Dog("Ha")
d.eat = "Meat"  # 给food赋值
d.eat           # 运行属性
del d.eat       # 删除赋值，不能直接删除，还需要在类里增加一个方法。
d.eat           # 会报错，因为删除没了。