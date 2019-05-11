'''
函数的参数
- 位置参数
-可变参数
-关键字参数
-命名关键字参数
'''

def f1(a, b = 5, c = 10):
    return a + b *2 + c * 3
print(f1(1, 2, 3))

def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(f2(1, 2, 3))
print(f2())

def foo1():
    a = 5
foo1()

from random import randint

def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total
def add(a=0, b =0, c= 0):
    return a + b + c

print(roll_dice(3))
print(add())