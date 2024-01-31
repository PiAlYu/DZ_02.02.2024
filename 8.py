from itertools import product

k = 1
for i in product('щогба', repeat = 6):
    s = ''.join(i)
    if s == 'общага':
        print(k)
        break
    k += 1
