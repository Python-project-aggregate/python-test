'''
求两个字符串的最长公共子串
'''
# 先生成一个二维列表
def substrings():
    a = "abcdea"
    b = 'abcde'
    lst1 = len(a)
    lst2 = len(b)
    max = 0 # 最大值,默认为0
    lst = []
    record = { j:[i for i in a] for j in b}
    print(record)
    for i in range(lst1):
        for j in range(lst2):
            record[0][i +1] = a[i]
            record[j+1][0] = b[j]
            # record[0][0] = 0
            if a[i] == b[j]:
                m = 1
                if m > max:
                    record[j+1][i+1] = m
                    m += 1
                    lst.append(a[i])


    # lst.append(*record)


    # print(*record, sep = "\n")
    # print(lst)
if __name__ == '__main__':
    substrings()