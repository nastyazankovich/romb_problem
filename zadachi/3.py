from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def len_area(self):
        pass

    @abstractmethod
    def len_perimeter(self):
        pass


class Romb(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def len_area(self):
        return self.a * self.b

    def len_perimeter(self):
        return 4 * self.a


romb = Romb(1, 2)
area = romb.len_area()
perimeter = romb.len_perimeter()

print("Площадь", area)
print("Периметр", perimeter)
