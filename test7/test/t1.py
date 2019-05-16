# 随机整数生成类
import random
class Test1:
    def __init__(self, num=20, x=1, y=9):
        self.num = num
        self.x = x
        self.y = y
    def nums(self):
        lst = [random.randint(self.x, self.y) for i in range(self.num)]
        return lst

# def num(t, x, y):
#     nums  = [random.randint(x, y) for i in range(t)]
a = Test1(9,1,3).nums()
# print(a)
co = Test1().nums()
# print(co)
def col(co):
    lst = []
    for i in range(0,len(co), 2):
        tuple = ()

        lst.append((co[i], co[i+1]))
    print(lst)
col(co)



