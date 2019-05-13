# origin = [30, 20, 80, 40, 50, 10, 60, 70, 90]
# length = len(origin)
# print(length)
# d = {}
# for i, v in enumerate(origin):
#    # print(i+1, v)
#    d[i+1] = v
#    print(d)
#
# for j in range(length//2):
#     for x in range(length):
#
#     print(d[j])

# a =[1, 2, 3, 4, 5, 6]
# b = len(a) + 1# 7
# c = len(a)//2 # 3
#
# record = [[0 for i in range(b)] for j in range(3)]
# # print(record)
# for i in range(c):
#     for j in range(b):
#         record[i][3] = a[0]
#         record[i][1] = a[1]
#         record[i][0] = a[3]
# #
# print(*record, sep='\n')
#       1           1   7
#   2       3       3   4
# 1   1   1   1     7   2
#1 1 1 1 1 1 1 1    15
import  math
# origin = [30, 20, 80, 40, 50, 10, 60, 70, 90]
# record = [[0 for i in range(15)] for j in range(4)]
# a =[1, 2, 3, 4, 5, 6, 7, 8, 9]

# math.log2()
# # lst = [str(i) for i in a]
# # b = ''.join(lst)
# start = 0
# stop = 1
# lst1 = []
# for i in range(3):
#     stop = (1 if i ==0 else 3 * i)
#     # for j in range(1):
#     # print(a[start:stop])
#     lst = [str(i) for i in a[start:stop]]
#     lst1.append(lst)
#     # print(' '.join(lst).center(7))
#     start = stop
# # print(lst1)
# for i in lst1:
#     for j in i:
#
#         print('{}{}'.format(' '*6,j),end=' ')
#     print()

import math
origin = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
n = len(origin) - 1
