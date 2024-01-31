fin = open('17 (1).txt')
s = fin.readlines()
fin.close()
s = [int(i) for i in s]
mi, ma, k = float('inf'), -float('inf'), 0
for i in s:
    if i % 103 == 0:
        mi = min(mi, i)
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) % 2 == 0 and abs(s[i] - s[i + 1]) % mi == 0:
        k += 1
        ma = max(ma, s[i] + s[i + 1])
print(k, ma)
