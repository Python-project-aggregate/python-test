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
        pre = 2** i - 1
