# 模拟购物车购物

import json
import re


class ShoppingCart:
    def __init__(self, num, name, color, price):
        self.num = num
        self.name = name
        self.color = color
        self.price = price

    def add(self):
        '''增加商品到购物车'''
        a = list()
        d = {self.num: {'名字': self.name, '颜色': self.color, '价格': self.price}}
        a.append(d)
        # print(type(d))
        '''写入json文件中'''
        with open('shopping.txt', 'r+') as f:
            if f.read():
                with open('shopping.txt', 'r+') as f1:
                    load_dict = json.load(f1)
                    f.seek(0)
                    f.truncate()
                    for i in load_dict:
                        a.append(i)
                json.dump(a, f, ensure_ascii=False)
            else:
                json.dump(a, f, ensure_ascii=False)
        print(a)

    @classmethod
    def shop(self):
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            for i in load_:
                for _, v in i.items():
                    print('{} {:10} {:5} {:5}'.format(_, v['名字'], v['颜色'], v['价格']))

    @classmethod
    def get_money(self, num):
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            # a = filter(lambda x:x[1],load_)
            for i in load_:
                for _, v in i.items():
                    if v['名字'] == '小米9':
                        print('结算第{}个商品{}:{}'.format(_, v['名字'], v['价格']))
                        del _

    @classmethod
    # @property
    def accounts(self, num=0):
        '''总计金额'''
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            for v in load_:
                for j in v.values():
                    print(j['名字'], j['价格'])
                    num += j['价格']
            print('总计金额为', num)

    @classmethod
    def clr(self, k):
        '''删除单个购物车物品'''
        # 正则匹配  {"67": {"名字": "小米9", "颜色": "blue", "价格": 2999}},
        with open('shopping.txt', 'r') as f:
            a = f.read()
            file = re.sub('{"' + k + '".+?}}', '', a, 1)
            with open("shopping.txt", 'w') as f1:
                f1.write(file)
        # 匹配,空格 清理干净
        # f.sub('{"' + k + '".+?}}', '', a, 1)
        # f = open("shopping.txt", 'w')
        # f.write(s)

    @classmethod
    def dele(self):
        '''清空购物车'''
        with open('shopping.txt', 'r+') as f:
            f.truncate()


if __name__ == '__main__':
    # ShoppingCart.shop()# 打印当前购物车
    # ShoppingCart(5,'macbook pro', 'white', 12588).add() # 添加商品到购物车
    # ShoppingCart.accounts() # 结算全部购物车商品
    ShoppingCart.get_money('小米9')  # 结算单个商品
    # ShoppingCart.clr('1') # 删除单个商品
    # ShoppingCart.dele()  # 清空购物车
