def foo1():
    msg = 'zen of python'
    def foo2():
        print(msg)
    return foo2
a = foo1()
def fun():
    print(5)
print(fun.__closure__)
print(a.__closure__[1].cell_contents)
