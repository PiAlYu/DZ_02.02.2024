def f(n):
    if n <= 2: return n
    return g(n) + f(n - 2)

def g(n):
    if n <= 2: return n
    return f(n - 1) - g(n - 2)

print(g(15))
