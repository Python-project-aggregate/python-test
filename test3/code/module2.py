# import module1
# 导入module时, 不会执行模块if条件成立时的代码因为模块的名字是module2而不是main
def foo():
    b = 'hello'
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar()

# if __name__ == '__main__':
#     a = 100
#     foo()
