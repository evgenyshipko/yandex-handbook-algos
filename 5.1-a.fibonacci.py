
def fib(n):
    if n < 2:
        return n
    prev = 0
    curr = 1

    i = 1
    while i < n:
        temp = prev
        prev = curr
        curr = curr + temp
        i += 1

    return curr


# assert fib(3) == 2
# assert fib(10) == 55

n = int(input())
print(fib(n))