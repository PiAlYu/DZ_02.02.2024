def f(n):
    s = 0
    while n > 0:
        s += n % 7
        n = n // 7
    return s

a = 51 * 7 ** 12 - 7 ** 3 - 22
print(f(a))
