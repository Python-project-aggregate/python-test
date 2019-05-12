import queue

q = queue.Queue()
q.put(1)
q.put('abc')
print(q.get())
# print(q.get())
# print(q.get(True, 5))# 同步阻塞 True 是等 ,成功拿到数据不会抛异常
print(q.get_nowait())# 同步阻塞
# 多线程可以打开,
print(q.get(True))