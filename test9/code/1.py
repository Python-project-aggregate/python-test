import math
import json


class Shape:
    def __init__(self, a, b, c = 2):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        raise NotADirectoryError()
class Triangle(Shape):  # 三角子类
    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print('三角面积',s)


class Rectangle(Shape):  # 矩形子类
    def area(self):
        s = self.a * self.b
        print('矩形面积',s)


class Circular(Shape):  # 圆子类
    def area(self):
        s = self.c ** 2 * math.pi
        print('圆面积',s)
        json_s = json.dumps(s)
        print('序列化',json_s)


a = Triangle(1, 1, 1)
b = Rectangle(1, 2)
c = Circular(0, 0, 3)
c.area()
b.area()
a.area()