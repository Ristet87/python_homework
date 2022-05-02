# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one") "один" >>> num_translate("eight") "восемь" Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции
# или снаружи.


eng_figures = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
rus_figures = ('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')

def num_translate():
    figure = str(input('Введите число от 0 до 10: '))
    if figure in eng_figures:
        print(rus_figures[eng_figures.index(figure)])
    elif figure in rus_figures:
        print(eng_figures[rus_figures.index(figure)])
    else:
        print(None)


num_translate()