
def get_max_profit(billboards, weeks, data):

    max_profit = 0

    # важно сортировать не только по цене, но и если цены равные, то по неделям (из-за этого не проходил 9-й тест)
    data = sorted(data, key=lambda x: (x[0], x[1])) # сортируем, чтобы каждый раз не искать максимум за линейное время

    w = 0
    while w < weeks:
        b = 0
        max_index = len(data) - 1
        while b < billboards and max_index >= 0:
            max_profit += data[max_index][0]

            print('b',b,'w',w, 'max_index',max_index,'data',data)

            data[max_index][1] -= 1
            if data[max_index][1] == 0:
                del data[max_index]

            max_index -= 1
            b += 1
        w += 1

    return max_profit


# billboards = 2
# weeks = 3
# data = [
#     [5, 1],
#     [2, 2],
#     [4, 3],
#     [1, 3]
# ] # [price for week, weeks]
#
# assert get_max_profit(billboards, weeks, data) == 21

billboards = 3
weeks = 2
data = [
    [5, 1],
    [2, 2],
    [4, 3],
    [1, 3]
] # [price for week, weeks]

assert get_max_profit(billboards, weeks, data) == 18


# billboards = 1
# weeks = 1
# data = [
#     [1, 1],
# ] # [price for week, weeks]
#
# assert get_max_profit(billboards, weeks, data) == 1
#
# billboards = 4
# weeks = 3
# data = [
#     [1, 1],
#     [1, 1]
# ] # [price for week, weeks]
#
# assert get_max_profit(billboards, weeks, data) == 2


# [billboards, data_length, weeks] = list(map(int, input().split()))
#
# data = []
# count = 0
#
# while count < data_length:
#     piece_of_data = list(map(int, input().split()))
#     data.append(piece_of_data)
#     count += 1
#
# print(get_max_profit(billboards, weeks, data))