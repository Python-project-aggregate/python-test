class Property:
    def __init__(self, fn):
        self.fn = fn

    def __get__(self, instance, owner):
        self.fn = self.fn(instance)
        return self.fn

    def setter(self, fn):
        print('!!!!!!!!!!!',fn)
        return fn

    def __set__(self, instance, value):
        instance.__dict__['_data']= value
        print(value, '===========', instance)


class A:
    # u = Property()
    def __init__(self,data):
        self._data = data

    @Property  # data = Property(data(self))
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

a = A(8)
a.data = 20
print(a.data, '++++++++++')
print(a.__dict__)
