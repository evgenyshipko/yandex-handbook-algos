def print_num_arr(arr):
    print(str(len(arr)) + ' ' + ' '.join(map(lambda x: str(x), arr)))

n = int(input())

res = []

i = 0
j = 0
while True:
    if n - i * 5 - j * 10 < 0 and i == 0 and j != 0:
        break
    if n - i * 5 - j * 10 >= 0:
        res.append([10]*j + [5]*i + [1]*(n - j*10 - i*5))
        i += 1
        continue
    i = 0
    j += 1

# res.sort(key=lambda x:len(x))

print(len(res))

for arr in res:
    print_num_arr(arr)





