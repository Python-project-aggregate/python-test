import sys
import random
def main(code_len=4):
    all_char = '2225255333222'
    code  = ''
    last_pos = len(all_char) - 1
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_char[index]
    return code

def get_suffix(filename, has_dot=False):
    '''
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名

    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


if __name__ == '__main__':
    print(main())
    print(get_suffix('asdfaf.agfa'))