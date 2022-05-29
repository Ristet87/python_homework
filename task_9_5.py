class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Вы пишите ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Вы пишите карандашом')


class Handle(Stationery):
    def draw(self):
        print('Вы пишите маркером')

a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()