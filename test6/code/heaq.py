from queue import Queue
import threading
list()
def dispatcher(src):
    handlers = []
    queues = []
    def reg(handle):
        q = Queue()
        queues.append(q)
        t = threading.Thread(target=handle, args = (q,))
        handlers.append(t)
    def run():
        for t in handlers:
            t.start()
        for item in src:
            for q in queues:
                q.put(item)
    return reg, run
reg, run = dispatcher(load('/logs'))