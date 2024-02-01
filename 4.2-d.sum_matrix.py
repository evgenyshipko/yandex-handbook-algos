
# просуммировать матрицы одинакового размера
def sum_matrix(a, b):
    res = []

    for row_index in range(len(a)):
        row_a = a[row_index]
        row_b = b[row_index]
        row_c = []
        for col_index in range(len(row_a)):
            row_c.append(row_a[col_index] + row_b[col_index])
        res.append(row_c)

    return res

# a = [[1, 2, 3], [4, 5 ,6]]
# b = [[-1, -2, -3], [-4, -5, -6]]
# assert sum_matrix(a, b) == [[0, 0, 0],[0, 0, 0]]
# assert sum_matrix([[1,2,3]], [[4,5,6]]) == [[5, 7, 9]]


[n, m] = list(map(int, input().split()))
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

res = sum_matrix(a, b)

for i in range(len(res)):
    print(' '.join(map(lambda x: str(x), res[i])))