
import random
from queue import Queue
a = Queue()
a.put(random.randint(1, 100))
print(a)
print(a.get())