
class Cell:
    def __init__(self, args):
        self.args = int(args)

    def __add__(self, other):
        return Cell(self.args + other.args)

    def __sub__(self, other):
        return Cell(self.args - other.args) if other.args <= self.args \
            else print(f'Число {self.args - other.args} меньше ноля')

    def __mul__(self, other):
        return Cell(self.args * other.args)

    def __floordiv__(self, other):
        return Cell(self.args // other.args)

    def __truediv__(self, other):
        return Cell(self.args // other.args)

    def __str__(self):
        return f'{self.args}'

    def make_order(self, n):
        for el in range(self.args // n):
            print('*' * n)
        print('*' * (self.args % n))


a = Cell(21)
b = Cell(5)
c = a + b
d = a - b
e = a * b
f = a / b
print(c)
print(d)
print(e)
print(f)
a.make_order(5)