# 模拟购物车购物

import json


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
            print(load_)

    @classmethod
    def get_money(self, num):
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            # a = filter(lambda x:x[1],load_)
            for i in load_:
                # print(i[2])
                for _, v in i.items():
                    if v['名字'] == '小米9':
                        print(_)
                # print(i)
            # print(a)

    @classmethod
    def accounts(self, num=0):
        '''总计金额'''
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            for v in load_:
                for j in v.values():
                    print(j['价格'])
                    num += j['价格']
            print('总计金额为', num)

    @classmethod
    def clr(self):
        '''删除购物车物品'''
        with open('shopping.txt', 'r+') as f:
            load_ = json.load(f)
            for i in load_:
                print(i)

    @classmethod
    def dele(self):
        '''清空购物车'''
        with open('shopping.txt', 'r+') as f:
            f.truncate()


if __name__ == '__main__':
    pass
    # ShoppingCart.shop()# 打印当前购物车
    # ShoppingCart(3,'气垫鞋', 'red', 80).add() # 添加商品到购物车
    # ShoppingCart.accounts() # 结算全部购物车商品
    ShoppingCart.get_money('小米9')  # 结算单个商品
    # ShoppingCart.clr() # 删除单个商品
    # ShoppingCart.dele() # 清空购物车
