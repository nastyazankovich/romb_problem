class A:
    def method(self):
        print('Method jf class A')


class B:
    def method(self):
        print('Method jf class B')


class C:
    def __init__(self):
        self.a = A()
        self.b = B()

    def method(self):
        self.a.method()
        self.b.method()


obj = C()
obj.method()
