class Figura:
    def __init__(self):
        pass


class Kvadrat(Figura):
    def __init__(self, a):
        super().__init__()
        self.a = a


class Romb(Kvadrat):
    def __init__(self, a):
        super().__init__(a)


romb = Romb(5)
print(romb)
