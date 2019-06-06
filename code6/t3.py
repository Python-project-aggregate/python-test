# 车辆信息
class Car:
    # _num = 0

    def __init__(self, mark='vov', color='red', price=100000, speed='140km/h'):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


def main(car):
    d = {}
    with open('car.txt', 'a+', encoding='utf-8') as f:
        d[car.mark] = '颜色:{} 价格:{} 速度:{}'.format(car.color, car.price, car.speed)
        print(d, file=f)
    print(d)


if __name__ == '__main__':
    a = Car('l', 'red', 400000, '170km/h')
    # print(a)
    main(a)
