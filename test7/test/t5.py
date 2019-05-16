# 模拟购物车购物
'''
添加购物车
删除购物车
一起清算
'''
import json
class ShoppingCart:
    def __init__(self, num, name, color, price):
        self.num = num
        self.name = name
        self.color = color
        self.price = price

    def add(self):
        '''增加商品'''
        a = list()
        d ={'序号':self.num,'名字':self.name, '颜色':self.color, '价格':self.price}
        a.append(d)
        # print(type(d))
        '''写入json文件中'''
        with open('shopping.txt','r+') as f:
            if f.read():
                with open('shopping.txt', 'r+') as f1:
                    load_dict = json.load(f1)
                    f.seek(0)
                    f.truncate()
                    for i in load_dict:
                        a.append(i)
                    # print(a)
                json.dump(a, f, ensure_ascii=False)
            else:
                json.dump(a, f, ensure_ascii=False)

    @classmethod
    def accounts(self):
        with open('shopping.txt','r+') as f:
            load_ = json.load(f)
            print(type(load_),load_)
            for i in f:

                print(load_)
a = ShoppingCart(5,'小米9', 'blue', 2999)
a.add()
ShoppingCart.accounts()
