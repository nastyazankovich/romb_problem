class A:
    def method(self):
        print('Method of class A')


class B:
    def method(self):
        print('Method of class B')


class C:
    def method(self):
        print('Method of class C')


class D(A, B, C):
    def method(self):
        super().method()
        print('Method of class D')


obj = D()
obj.method()
