# 堆排序
import math
def print_tree(array, unit_width=2):
    '''

    :param array:
    :param unit_width:
    :return:
    '''
    length = len(array)
    index = 1
    depth = math.ceil(math.log2(length))
    space = ' '* unit_width
    for i in range(depth-1, -1, -1):
        pre = 2 ** i - 1
        print(pre * space, end = '')
        offset = 2 ** (depth - 1 -1 )
        line = array[index:index + offset]
        interval = (2 * pre + 1) * space
        print(interval.join(map(lambda x :"{:2}".format(x), line)))
        index += offset

origin = [0, 30, 20, 80, 40,50, 10, 60, 70, 90]
total = len(origin) - 1