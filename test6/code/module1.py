from pathlib import Path
import datetime
import re
pattern = '''(?p<remote>[\d.]{7,} - - \[(?p<datetime>[\w/: +]+\] \ 
"(?p<method>\w+) (?p<url>\s+) (?p<protocol[\w\d/.]+>)") (?p<status>\d+)'''
regex = re.compile(pattern)
conversion = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr,%d/%b/%Y:%H:%M:%S%z), 'status': int, 'length':int
}
def extract(logline:str) -> dict:
    m = regex.match(logline)
    if m:
        return {k:conversion.get(k, lambda x:x)(v) for k,v in m.groudict().items()}
    else:
        return None
def loadfile(filename:str, encoing='utf-8'):
    with open(filename, encoding=encoing) as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue

def load(*path, encoding='utf-8', ext='*.log', recursive=False):
    for x in paths:
        print(x)
        p = Path(x)
        if p.is_dir():
            if isinstance(ext, str):
                ext = [ext]
            else:
                ext = list(ext)
            for e in ext:
                files = p.rglob(e) if recursive else p.glob(e)
                for file in files:
                    yield from loadfile(str(file.absolute()), encoding=encoding)
        elif p.is_file():
            yield from loadfile(str(p.absolute()), encoding = encoding)

