from queue import Queue
import threading
from pathlib import Path
def load(*parhs, endcoding= 'utf-8', ext='*.log', recursive=False):
    for x in paths:
        p = Path(x)
        if p.is_dir():

def dispather(src):
    handlers = []
    queues = []
    def reg(handle):
        q = Queue()
        queues.append(q)
        t = threading.Thread(target=handle,args = (q,))
        handlers.append(t)
    def run():
        for t in handlers:
            t.start()
        for item in src:
            for q in queues:
                q.put(item)
    return reg, run
reg, run = dispather(load'/logs')
