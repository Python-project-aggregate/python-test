# 模拟购物车购物

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age
    def age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

tom = Person('tom')
print(tom.age())
tom.set_age(20)