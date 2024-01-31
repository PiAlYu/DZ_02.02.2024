def f(n):
    for i in range(2, 7):
        if n % i == 0:
            return n // i

for i in range(224770, 664423, 455):
    if i % 25 != 0 and i % 49 != 0 and i % 169 != 0:
        if f(i) <= 100000 and f(i) % 100 == 19:
            print(i, f(i))
