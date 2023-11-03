from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def method(self):
        pass


class B(A):
    def method(self):
        print('Method of class B')


class C(A):
    def method(self):
        print('Method of class C')


class D(B, C):
    def method(self):
        super().method()
        print('Method of class D')


obj = D()
obj.method()
