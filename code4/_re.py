import queue
import threading
import time

a = [1, 2, 3]
q = queue.Queue()
q.put(1)
q.put('abc')
# q.put(a)
print(q.get())
print(q.get())
# print(q.get())
def handle(q:queue.Queue):
    time.sleep(5)
    q.put('xyz')
t = threading.Thread(target =handle,args = (q,))
t. start() # 启动
print(q.get()) # empty

