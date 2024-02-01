from array import array


def find_min_index(arr, start):
    min_val = arr[start]
    index = start
    for i in range(start, len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
            index = i
    return index


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = find_min_index(arr, i)
        swap(arr, i, min_index)
    return arr


n = input()

nums_str = input().split(' ')

if len(nums_str) != int(n):
    raise Exception('n different from arr length', n , len(nums_str))

nums = map(lambda x: int(x), nums_str)

sorted_nums_arr = selection_sort(array('i', nums))

sorted_nums_arr_str = map(lambda x: str(x), sorted_nums_arr)

print(' '.join(sorted_nums_arr_str))