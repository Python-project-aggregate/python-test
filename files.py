filename = 'sample.txt'
d = {}
with open(filename, encoding='utf-8') as f:
    for line in f:
        words = line.split()