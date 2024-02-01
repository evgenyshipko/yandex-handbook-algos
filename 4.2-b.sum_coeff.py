# Необходимо просуммировать коэффициенты двух многочленов

def sum_coeff(a, b):

    counter = 0

    result = []

    while counter < len(a) and counter < len(b):
        a_i = a[len(a) - counter - 1]
        b_i = b[len(b) - counter - 1]
        result.insert(0, a_i+b_i)
        counter += 1

    if counter < len(a):
        result = a[0: len(a) - counter] + result
    if counter < len(b):
        result = b[0: len(b) - counter] + result

    return result


assert sum_coeff([1, 2, 3, 4], [1, 0, 0]) == [1, 3, 3, 4]
assert sum_coeff([1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
assert sum_coeff([1, 1], [1, 1]) == [2, 2]


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

print(n if n >= m else m)
print(' '.join(map(lambda x: str(x), sum_coeff(a, b))))