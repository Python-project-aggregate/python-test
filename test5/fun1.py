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
print(origin)
print_tree(origin)
print('='* 50 )
def heap_adjust(n, i, array:list):
    while 2 * i <= n:
        lchile_index = 2 * i
        max_child_index = lchile_index
        if n> lchile_index and array[lchile_index + 1] > array[lchile_index]:
            max_child_index = lchile_index+ 1
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break
def max_heap(total, array:list):
    for i in range(total // 2, 0, -1):
        heap_adjust(total, i, array)
    return array
print_tree(max_heap(total, origin))
print('=', 50)
def sort(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total -1]:
            break
        heap_adjust(total, 1, array)
print_tree(sort(total, origin))
print(origin)