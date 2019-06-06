class Property:
    def __init__(self, getmethod=None, setmethod=None):
        self.getMethod = getmethod
        self.setMethod = setmethod

    def __get__(self, ins, cls):
        return self.getMethod(ins)

    def __set__(self, ins, val):
        self.setMethod(ins, val)

    def setter(self, setmethod):
        return type(self)(self.getMethod, setmethod)


class A:
    def __init__(self, name):
        self._name = name

    @Property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


t = A('hpl')
print(t.name)
t.name = 'new_hpl'
print(t.name)