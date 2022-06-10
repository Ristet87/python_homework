from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def count_rate(self):
        pass


class Coat(Dress):

    def __add__(self, other):
        return Coat(self.size + other.size)

    def __str__(self):
        return f'{self.size}'

    @property
    def count_rate(self):
        self.size = self.size/6.5 + 0.5
        return self.size


class Suit(Dress):

    @property
    def count_rate(self):
        self.size = 2 * self.size + 0.3
        return self.size


a = Coat(42)
b = Suit(2)

print(a.count_rate)
print(b.count_rate)
print(a + b)
