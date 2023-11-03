class Tochka:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Romb:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


a = Tochka(0, 0)
b = Tochka(1, 1)
c = Tochka(2, 2)
d = Tochka(3, 3)
romb = Romb(a, b, c, d)

print(romb.a.x, romb.a.y)
print(romb.b.x, romb.b.y)
print(romb.c.x, romb.c.y)
print(romb.d.x, romb.d.y)
