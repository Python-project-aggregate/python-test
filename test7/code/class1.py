class Person:
    pass
def addname(name, cls):
    cls.NAME = name
addname('xyz', Person)
def addname(name):
    def wrapper(cls):
        cls.NAME = name

    return wrapper
a = Person()
print(a.NAME)