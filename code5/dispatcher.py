from queue import Queue
import threading
from pathlib import Path
def load(*parhs, endcoding= 'utf-8', ext='*.log', recursive=False):
    for x in paths:
        p = Path(x)
        if p.is_dir():
            if isinstance(ext, str):
                ext = [ext]
            else:
                ext = list(ext)
            for e in ext:
                files = p.rglob(e) if recursive else p.glob(e)
                with file.open(encoding=endcoding) as f:
                    for line in f:
                        fields = extract(line)
                        if fields:
                            yield fields
                        else:
                            continue
        elif p.is_file():
            pass
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
