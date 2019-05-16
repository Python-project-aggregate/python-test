# 车辆信息
class Car:
    _num = 0

    def __init__(self, mark='vov', color=0, price=0, speed=0):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed

    def add_car(self):
        d = {}
        d[self.mark] = '{}-{}-{}'.format(self.color, self.price, self.speed)
        print(d, )

if __name__ == '__main__':

    a = Car('1', 0, 0, 0)
    a.add_car()
