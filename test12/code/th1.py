# 数据结构和GIL
# 标准库Queue是线程安全的,适用于多线程安全的交换数据, 内部使用了LOck和Condition
# QUeue类的size虽然加了锁,但是依然不能保证get. put就能成功, 因为读取大小和get, put方法是分开的
# import queue
# q = queue.Queue(8)
# if q.size() == 7:
#     q.put()

# if q.qsize() == 1:
#     q.get()

import logging
import datetime
logging.basicConfig(level = logging.INFO, format = '%(thread)s %(message)s')
start = datetime.datetime.now()
def calc():
    sum = 0
    for _ in range(100000000):
        sum += 1

calc()
calc()
calc()
calc()
delta = (datetime.datetime.now() - start.total_second()