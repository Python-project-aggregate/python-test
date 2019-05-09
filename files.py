filename = 'sample.txt'
d = {}
with open(filename, encoding='utf-8') as f:
    for line in f:
        words = line.split()
        for word in map(str.lower, word):
            d[word] = d.get(word, 0) + 1
print(sorted(d.items(), key = lambda item:item[1], reverse=True))
from collections import defaultdict
d = defaultdict(lambda :0)
with open(filename, encoding='utf-80') as f:
