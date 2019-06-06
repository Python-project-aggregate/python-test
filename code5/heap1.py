import math
# 打印树
def print_tree(array, unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length+1))
    index = 1
    width = 2 ** depth -1
    for i in range(depth):
        for j in range(2**i):
            print('{:^{}}'.format(array[index],width * unit_width),end=' '*unit_width)
            index +=1
            if index >= length:
                return
        width = width // 2
        print()
# origin = [0, 30, 20, 80, 40, 50, 10, 60, 70, 90]
origin = [0, 30, 20, 80, 90, 50, 10, 60, 70, 40]
total = len(origin) - 1 # 初始待排元素个数, 即n
print(origin)
print_tree(origin)
def heap_adjust(n ,i, array:list):
    '''
    调整的结点起点在n // 2, 保证所有调整的结点都有孩子
    :param n: 待比较个数
    :param i: 当前结点的下标
    :param array: 待排序数据
    :return: None
    '''
    while 2 * i <= n:
        lchild_index = 2 * i
        max_child_index = lchild_index # n= 2i
        if n > lchild_index and array[lchild_index + 1] > array[lchild_index]:
            max_child_index = lchild_index + 1
        if array[max_child_index] > array[i]:
            array[i], array[max_child_index] = array[max_child_index], array[i]
            i = max_child_index
        else:
            break
# print()
# heap_adjust(total, 1, origin)
# print_tree(origin)
def max_heap(total, array:list):
    for i in range(total//2, 0, -1):
        heap_adjust(total, i, array)
    return array
# print_tree(max_heap(total,origin))
def sort(total, array:list):
    while total > 1:
        array[1], array[total] = array[total], array[1]
        total -= 1
        if total == 2 and array[total] >= array[total - 1]:
            break
        heap_adjust(total, 1, array)
    return array
print_tree(sort(total, origin))
# print(origin)