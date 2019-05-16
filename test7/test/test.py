import json
import re
file = open('shopping.txt', 'r')
a = file.read()
s = re.sub(r"2", '66',a, 1)
f = open("shopping.txt",'w')
f.write(s)