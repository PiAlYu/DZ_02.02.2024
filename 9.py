class Digit:
    def __init__(self, x1, x2, x3, x4, x5):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
    def a(self):
        l = [self.x1, self.x2, self.x3, self.x4, self.x5]
        c = 0
        for i in l:
            if l.count(i) == 2:
                c += 1
        return c == 4
    def b(self):
        l = [self.x1, self.x2, self.x3, self.x4, self.x5]
        x, x1, x2 = 0, 0, 0
        s = set()
        for i in l:
            if l.count(i) == 1:
                x = i
            else:
                s.add(i)
        s = list(s)
        print(s)
        return max(s) > x and min(s) < x

fin = open('10.csv')
s = fin.readlines()
fin.close()
s = [i.split(';') for i in s]
print(s)
a, k = [], 0
for i in s:
    a.append(Digit(int(i[0]), int(i[1]), int(i[2]), int(i[3]),int(i[4])))
for i in a:
    if i.a() and i.b() == True:
        k += 1
print(k)
