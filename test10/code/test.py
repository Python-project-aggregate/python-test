class A:
    def __init__(self):
        self.a1 = 'a1'
    def __get__(self, instance, owner):
        return 3

    def __set__(self, instance, value):
        self.instance  = 88
        print(instance, value,'__________--')
        return 30


class B:
    u = A()
    def __init__(self):
        self.x= '56'


b = B()
b.u = 10
# print(b.__dict__)
# print(b.u) # __getattribute__做判断  是个类 是实现了__call__方法
# print(type(b).__dict__['x'].__get__(b, type(b)))# 非数据描述器
