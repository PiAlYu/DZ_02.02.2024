fin = open('27B.txt')
s = fin.readlines()
fin.close()
s.pop(0)
s = [int(i) for i in s]
k = 0
a = [0] * 131
for i in s:
    k += a[(131 - (i % 131)) % 131]
    a[i % 131] += 1
print(k)
