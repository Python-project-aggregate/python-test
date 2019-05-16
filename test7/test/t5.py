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
        d = {}
        d[self.num]={'名字':self.name, '颜色':self.color, '价格':self.price}
        # print(d)
        dump_dict = json.dumps(d,ensure_ascii=False)
        '''写入json文件中'''
        with open('shopping.json') as f:
            if f.read():
                f.close()
                with open('shopping.json', 'r+') as f1:
                    loads_dict = json.load(f1)
                    print(loads_dict,type(loads_dict))
                    dump_dict = loads_dict + ',' +dump_dict
                    json.dump(dump_dict, f1, ensure_ascii=False)
            else:
                with open('shopping.json', 'w+') as f1:
                    json.dump(dump_dict, f1, ensure_ascii=False)



    @classmethod
    def accounts(self):
        with open('shopping.json') as f:
            load_dict = json.load(f)
        loads_dict = json.loads(load_dict)
        print(load_dict)


a = ShoppingCart(1,'小米9', 'blue', '2999')
a.add()
# ShoppingCart.accounts()
