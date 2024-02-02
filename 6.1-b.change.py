def print_num_arr(arr):
    print(' '.join(map(lambda x: str(x), arr)))


nominals = [50, 20, 10, 5, 1]
def change(n, noms):
    result = []

    while n > 0:
        for nom in noms:
            if n - nom >= 0:
                n -= nom
                result.append(nom)
                break

    return result

n = int(input())
arr = change(n, nominals)
print(len(arr))
print_num_arr(arr)