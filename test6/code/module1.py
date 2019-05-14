from pathlib import Path
import datetime
import re
pattern = '''(?p<remote>[\d.]{7,} - - \[(?p<datetime>[\w/: +]+\] \ 
"(?p<method>\w+) (?p<url>\s+) (?p<protocol[\w\d/.]+>)")'''
regex = re.compile(pattern)
conversion = {
    'datetime': lambda timestr: datetime.datetime.strptime(timestr,%d/%b/%Y:%H:%M:%S%z), 'status': int, 'length':int
}