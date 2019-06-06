class Property:
    def __init__(self, get_fn =None , set_fn = None):
        self.get_fn = get_fn
        self.set_fn = set_fn
    def __get__(self, instance, owner):
        return self.get_fn(instance)

    # def __set__(self, instance, value):
    #     self.set_fn(instance, value)

    def setter(self, set_fn):
        print(type(self)(self.get_fn, set_fn))
        return type(self)(self.get_fn, set_fn)

class A:

    def __init__(self,data):
        self._data = data

    @Property  # data = Property(data(self))
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

a = A(8)
print(a.data, '++++++++++')
a.data = 20
print(a.data, '++++++++++')

