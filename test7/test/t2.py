# 打印坐标
from t1 import Test1
import numpy as np
import matplotlib.pyplot as plt

co1 = Test1().nums()
'''随机生成20个数字,调用已经写好的t1模块'''


class Test2:

    def col(co):
        lst = []
        for i in range(0, len(co), 2):
            lst.append((co[i], co[i + 1]))
        print(lst)

    # @staticmethod
    def mat(lst1):
        x, y = list(), list()
        for i in range(0, len(co1), 2):
            x.append(co1[i])
            y.append(co1[i + 1])
        x1 = np.array(x)
        y1 = np.array(y)

        plt.scatter(x1, y1)
        plt.show()

if __name__ == '__main__':

    # random_num = Test2()
    a = Test2.col(co1)
    b = Test2.mat(a)
