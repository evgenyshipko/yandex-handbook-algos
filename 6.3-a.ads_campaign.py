def max_index(arr):
    max_index = 0
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max_index = i
            max = arr[i]
    return max_index


def max_sum(prices, clicks):
    sum = 0

    while len(prices) > 0:
        max_index_price = max_index(prices)
        max_index_clicks = max_index(clicks)
        sum += prices[max_index_price] * clicks[max_index_clicks]
        del prices[max_index_price]
        del clicks[max_index_clicks]

    return sum

# assert max_sum([0, 1], [1, 0]) == 1
# assert max_sum([0,0,0,0], [1, 2, 3, 4]) == 0
# assert max_sum([10, 20, 30],[3, 2 ,1]) == 140

n = input() #для валидатора
prices = list(map(int, input().split()))
clicks = list(map(int, input().split()))

res = max_sum(prices, clicks)

print(res)
