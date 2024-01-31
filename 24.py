fin = open('24.txt')
s = fin.readline()
fin.close()
k, ma = 1, 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        k += 1
    else:
        ma = max(ma, k)
        k = 1
ma = max(ma, k)
print(ma)
