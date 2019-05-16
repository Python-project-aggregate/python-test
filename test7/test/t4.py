# 温度转换
class Chage:
    def __init__(self, hua_style=0, c=0, open=0):
        self.hua_style = hua_style
        self.c = c
        self.open = open

    def tem1(self):
        '''华氏温度转换为摄氏温度'''
        self.c = 5 * (self.hua_style - 32) / 9
        print('摄氏温度为', self.c)

    def tem2(self):
        '''摄氏温度转换为华氏温度'''
        self.hua_style = (9 * self.c) / 5 + 32
        print('华氏温度为', self.hua_style)

    def tem3(self):
        '''摄氏温度转换为开式温度'''
        self.open = self.c + 273.15
        print('开式温度为', self.open)


if __name__ == '__main__':
    Chage(hua_style=33).tem1()
    Chage(c=33).tem2()
    Chage(open=33).tem3()
