def heap_sort(list):
    for start in range((len(list)- 2)//2, -1, -1):
        sift_down(list, start, len(list)-1)
    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        sift_down(list, 0, end - 1)
    return list
def sift_down(lst, n, i):
    root = n
    while True:
        child = 2 * root + 1
        if child > i:
            break
        if child + 1<= i and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break
lst = [2, 6, 5, 4, 3, 8, 1, 9, 7]
print(heap_sort(lst))