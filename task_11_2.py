class ZeroDivide(Exception):
    def __init__(self, txt):
        self.txt = txt

    divident = int(input('Введите делимое: '))
    divider = int(input('Введите делитель: '))

    try:
        res = divident / divider
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    else:
        print(f'Частное {res}')

