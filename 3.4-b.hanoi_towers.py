# Ханойские башни. Рекурсия.

# Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3.
# Также в головоломке используется стопка дисков с отверстием посередине.
# Радиус дисков уменьшается снизу вверх. Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу.
# Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, только если он пустой или верхний диск на нём большего размера, чем перемещаемый.
# Цель головоломки — перенести все диски со стержня 1 на стержень 3.
#
# Немного изменим правила. Теперь головоломка состоит из четырех стержней,
# а цель головоломки — перенести все диски со стержня 1 на стержень 4.
# Найдите минимальное количество ходов, за которое можно решить головоломку.

def findK(n):
    sum = 0
    counter = 0
    while sum + counter + 1 <= n:
        counter += 1
        sum += counter

    return counter


def hanoiTowersThreeCount(n):

    operations = 0

    def hanoiTowersThree(n, fromPeg, toPeg):
        nonlocal operations

        operations += 1

        if n == 1:
            return 1

        unusedPeg = 6 - fromPeg - toPeg

        hanoiTowersThree(n-1, fromPeg, unusedPeg)

        hanoiTowersThree(n-1, unusedPeg, toPeg)

    hanoiTowersThree(n, 1, 3)

    return operations


def hanoiTowersFourCount(n):

    if n == 1:
        return 1

    k = findK(n)

    return 2 * hanoiTowersFourCount(n - k) + hanoiTowersThreeCount(k)

n = input()

print(hanoiTowersFourCount(int(n)))