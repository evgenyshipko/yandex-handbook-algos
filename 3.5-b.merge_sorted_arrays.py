from array import array

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

def merge(list_of_arrays):
    result_arr = list_of_arrays[0]
    index = 1
    while index < len(list_of_arrays):
        result_arr = merge_sorted_arrays(result_arr, list_of_arrays[index])
        index += 1
    return result_arr


list_count = int(input())

counter = 0

list_of_arrs = []

while counter < list_count:
    num = int(input())
    str_arr = input().split(' ')

    if num != len(str_arr):
        raise Exception('num different from arr length', num, len(str_arr))

    num_arr = list(map(lambda x: int(x), str_arr))

    # сортируем входные массивы, т.к. в тренажере баг (или спецом корявые данные подают)
    num_arr.sort()

    list_of_arrs.append(num_arr)
    counter += 1

merged_lists = merge(list_of_arrs)

print(' '.join(map(lambda x: str(x), merged_lists)))







