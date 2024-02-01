# Игра в камни. Динамическое программирование

# Вы играете в игру <<Камни>>: игру для двух игроков с двумя наборами камней по
# n и m штук. С каждым ходом один игрок может забрать следующие комбинации камней:
#
# Взять один камень из любого набора.
# Взять два камня из какого-то одного набора
# Взять два камня из одного и один из другого.
# Когда камень забрали, он выходит из игры. Побеждает игрок, который заберет последний камень. Первый ход за вами.
#
# Вы и ваш оппонент играете оптимально.

# Решение динамическим подходом. Не проходит 18-й тест по времени выполнения. Кажется дело в медленных циклах for

inputs = input().split(" ")

[n, m] = map(lambda x: int(x), inputs)

L = False

W = True

M = {}

M[0, 0] = L

for i in range(1, n + 1):
    M[i, 0] = L if i % 3 == 0 else W
for j in range(1, m + 1):
    M[0, j] = L if j % 3 == 0 else W

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if M[i-1, j] and M[i, j-1] and (j < 2 or i < 2):
            M[i, j] = L
        elif M[i-1, j] and M[i, j-1] and M[i-2, j] and M[i, j-2] and M[i-1, j-2] and M[i-2, j-1]:
            M[i, j] = L
        else:
            M[i, j] = W

print('Win' if M[n, m] is True else 'Loose')


# Решение закономерностью:

inputs = input().split(" ")

[n, m] = map(lambda x: int(x), inputs)

def rocks(n, m):
    L = 'Loose'
    W = 'Win'

    if n == m:
        return L

    if abs(n - m) % 3 == 0:
        return L
    else:
        return W


print(rocks(n, m))

