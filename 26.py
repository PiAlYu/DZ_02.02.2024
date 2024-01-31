fin = open('26.txt')
s = fin.readlines()
fin.close()
a = int(s.pop(0).split()[0])
s = [int(i) for i in s]
s.sort(key = lambda x: -x)
k, mi = 0, 0
for i in s:
    if i <= a:
        a = a - i
        k += 1
        mi = i
print(k, mi)
