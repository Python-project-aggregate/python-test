# 求两个字符串的最大公共子串
# str1 = 'abcdef'
# str2 = 'jcdeg'
def get_max(str1: str, str2: str):
    lst1 = len(str1)
    lst2 = len(str2)
    record = [[0 for i in range(lst2 + 1)] for j in range(lst1 + 1)]
    max = 0  # 最长匹配长度
    p = 0  # 匹配的起始位
    for i in range(lst1):
        for j in range(lst2):
            if str1[i] == str2[j]:
                record[i + 1][j + 1] = record[i][j] + 1
                if record[i + 1][j + 1] > max:
                    max_num = record[i + 1][j + 1]
                    p = i + 1
                    # print(p-max_num, p)
    print(str1[p - max:p], max)


# print(*record, sep='\n')
if __name__ == '__main__':
    str1 = input(">>")
    str2 = input(">>")
    get_max(str1, str2)
