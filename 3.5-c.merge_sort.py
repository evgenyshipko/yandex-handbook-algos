import math

# computational complexity O(arr1.length + arr2.length)
# memory complexity O(arr1.length + arr2.length)
def merge_sorted_arrays(arr1, arr2):

    result = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] >= arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            result.append(arr2[j])
            i += 1
            j += 1

    if i < len(arr1):
        for index in range(i, len(arr1)):
            result.append(arr1[index])

    if j < len(arr2):
        for index in range(j, len(arr2)):
            result.append(arr2[index])

    return result

# computational complexity O(n * logn)
# memory complexity O(n * logn)

def merge_sort(arr: list):
    if len(arr) == 1:
        return arr

    mid = math.floor(len(arr)/2)

    sorted1 = merge_sort(arr[0: mid])
    sorted2 = merge_sort(arr[mid: len(arr)])

    return merge_sorted_arrays(sorted1, sorted2)

n = input() # ненужный ввод для тренажера

list_str = input().split(' ')

num_str = list(map(lambda x: int(x), list_str))

print(' '.join(map(lambda x: str(x), merge_sort(num_str))))