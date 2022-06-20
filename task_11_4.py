class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'

    def action(self):
        return 'Print'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Scan'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Copy'


store = Storage()

scaner = Scaner('hp', '321', 90)
store.add_to(scaner)
scaner = Scaner('hp', '311', 97)
store.add_to(scaner)
scaner = Scaner('hp', '330', 99)
store.add_to(scaner)
printer = Printer('e-320', 'sony', 126, 2018)
store.add_to(printer)

print(store._dict)

store.extract('Scaner')
print()
print(store._dict)
