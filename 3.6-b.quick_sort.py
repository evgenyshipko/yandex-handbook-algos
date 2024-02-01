import random
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def lomuto_permutation(arr):

    if len(arr) < 2:
        return 0

    first_bigger_index = None

    base_random_index = random.choice(range(len(arr)))

    FIRST_INDEX = 0

    swap(arr, base_random_index, FIRST_INDEX)

    base_element = arr[FIRST_INDEX]

    counter = FIRST_INDEX + 1

    while counter < len(arr):
        element = arr[counter]

        if element < base_element and first_bigger_index is not None:
            swap(arr, counter, first_bigger_index)
            first_bigger_index = first_bigger_index + 1
        elif element > base_element and first_bigger_index is None:
            first_bigger_index = counter
        counter += 1

    new_base_index = first_bigger_index - 1 if first_bigger_index is not None else FIRST_INDEX

    swap(arr, FIRST_INDEX, new_base_index)

    # print('base_random_index',base_random_index,'base_element',base_element, 'new_base_index',new_base_index,'arr',arr)

    return new_base_index


def quick_sort(arr):

    if len(arr) < 2:
        return arr

    base_index = lomuto_permutation(arr)

    sorted1 = quick_sort(arr[0: base_index])

    sorted2 = quick_sort(arr[base_index + 1: len(arr)])

    middle = arr[base_index]

    result = None

    if len(sorted1) == 0 and sorted2[-1] < middle:
        sorted2.append(middle)
        result = sorted2
    elif len(sorted2) == 0 and sorted1[-1] > middle:
        sorted1.insert(0, middle)
        result = sorted1
    else:
        result = sorted1 + [middle] + sorted2

    # print('base_index', base_index,'base',arr[base_index],'arr',arr,'sorted1',sorted1,'sorted2',sorted2, 'result',result )

    return result


assert quick_sort([13, 17, 37, 73, 31, 19, 23]) == [13, 17, 19, 23, 31, 37, 73]

assert quick_sort([18, 20, 3, 17]) == [3, 17, 18, 20]

assert quick_sort([1, 11, 1]) == [1, 1, 11]

assert quick_sort([10,1,9,2,8,3,7,4,6,5,0,100,200,300,-3]) == [-3,0,1,2,3,4,5,6,7,8,9,10,100,200,300]


# n = input() # ненужный ввод для тренажера
#
# list_str = input().split(' ')
#
# num_str = list(map(lambda x: int(x), list_str))
#
# print(' '.join(map(lambda x: str(x), quick_sort(num_str))))