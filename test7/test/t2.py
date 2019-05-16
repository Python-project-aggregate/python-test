from t1 import Test1
import matplotlib.pyplot as plt

class Test2:
    co = Test1().nums()
    '''随机生成20个数字,调用已经写好的t1模块'''

    def col(co):
        lst = []
        for i in range(0,len(co), 2):
            lst.append((co[i], co[i+1]))
        print(lst)
random_num = Test2()


