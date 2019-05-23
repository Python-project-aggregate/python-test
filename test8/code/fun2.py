
a = "1.汉堡类\n2.小食类\n3.饮料类\n0.结束点餐"
b = "1.香脆鸡腿堡\n2.香脆鸡腿堡\n3.新奥尔良烤翅腿堡\n4.半鸡半虾堡\n0.返回主菜单"
c =  "1.薯条\n2.黄金鸡块\n3.香甜栗米棒\n0.返回主菜单"
d = "1.可口可乐\n2.九珍果汁\n3.金典咖啡\n0.返回主菜单"

lst =  []
print(a)
while True:
    server = int(input("请选择服务:"))
    if server ==0:
        print('您点了{}感谢您的使用'.format(*lst))
        break
    if server == 1:
        print(b)
        servers = int(input('请选择商品:'))
        if servers == 1:
            print('您已选择'+'香脆鸡腿堡'+'请继续使用')
            lst.append('香脆鸡腿堡')
        if servers == 0:
            continue


    if server == 2:
        print(c)
        pass

    if server ==3:
        print(d)
        pass







