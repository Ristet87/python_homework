class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_salary = salary
        self.income_bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self.income_salary * 12 + self.income_bonus}'

a = Position('Ivan', 'Ivanov', 'Manager', 20, 100)
print(a.get_full_name())
print(a.get_total_income())
