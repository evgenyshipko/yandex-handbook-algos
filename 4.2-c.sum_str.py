
def sum(a,b):
    res = ''
    for i in range(len(a)):
        res += a[i] + b[i]
    return res


assert sum('abc','def') == 'adbecf'
assert sum('abaca','bdaef') == 'abbdaaceaf'
assert sum('y','x') == 'yx'


n = input()
a = input()
b = input()

print(sum(a, b))