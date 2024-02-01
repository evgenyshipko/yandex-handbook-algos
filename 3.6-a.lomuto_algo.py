import random
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def lomuto_permutation(arr):

    first_bigger_index = None

    base_random_index = random.choice(range(len(arr)))

    swap(arr, 0, base_random_index)

    base_element = arr[0]

    counter = 1

    while counter < len(arr):
        element = arr[counter]

        if element < base_element and first_bigger_index is not None:
            swap(arr, counter, first_bigger_index)
            first_bigger_index = first_bigger_index + 1
        elif element > base_element and first_bigger_index is None:
            first_bigger_index = counter
        counter += 1

    if first_bigger_index is not None:
        swap(arr, 0, first_bigger_index - 1)

    print('arr',arr, 'base_element',base_element)

    return arr


lomuto_permutation([4, 7, 2, 5, 3, 1, 8, 9, 6])

# assert lomuto_permutation([4, 7, 2, 5, 3, 1, 8, 9, 6]) == [1, 2, 3, 4, 7, 5, 8, 9, 6]

# assert lomuto_permutation([3, 4, 7, 17]) == [3, 4, 7, 17]
#
# assert lomuto_permutation([1, 3, 2, 9, 10]) == [1, 3, 2, 9, 10]


# n = input() # ненужный ввод для тренажера
#
# list_str = input().split(' ')
#
# num_str = list(map(lambda x: int(x), list_str))
#
# print(' '.join(map(lambda x: str(x), lomuto_permutation(num_str))))