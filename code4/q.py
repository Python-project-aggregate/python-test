import queue
import threading
from queue import Queue
def dispatcher():
    queues = []
    handles = []
    def reg(fn):
        q = Queue()
        queues.append(q)
        t = threading.Thread(target=fn, args=(q,))

    def run():
        for t in handles:
            t.start()

    return reg, run
reg, run = dispatcher()
def handle(q:Queue):
    while True:
        data = q.get()
        if data:
            pass


reg(handle)
run()