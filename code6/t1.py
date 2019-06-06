# 随机整数生成类
import random


class Test1:
    def __init__(self, num=20, x=1, y=9):
        '''
        初始化操作
        :param num: 数字的个数
        :param x: 数值范围的起点
        :param y: 数值范围的终点
        '''
        self.num = num
        self.x = x
        self.y = y

    def nums(self):
        lst = [random.randint(self.x, self.y) for i in range(self.num)]
        return lst


if __name__ == '__main__':
    a = Test1(9, 1, 3).nums()
    print(a)
