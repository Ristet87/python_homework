from itertools import zip_longest


class Matrix:
    def __init__(self, list_matrix):
        self.list_matrix = list_matrix

    def __str__(self):
        return '\n'.join(str(i) for i in self.list_matrix)

    def __add__(self, other):
        return Matrix([el_self + el_other for el_self, el_other in zip_longest(self_row, other_row)]
                      for self_row, other_row in zip_longest(self.list_matrix, other.list_matrix))


a = Matrix([[1, 2], [2, 4], [5, 3]])
b = Matrix([[1, 2], [1, 1], [1, 1]])
print(a + b)
