class Figura:
    def len_area(self):
        pass


class Diagonal:
    def len_length(self):
        pass


class Romb(Figura, Diagonal):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def len_area(self):
        return self.a * self.b

    def len_length(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5


romb = Romb(8, 8)

area = romb.len_area()
lengh = romb.len_length()

print("Площадь", area)
print("Диагональ", lengh)
