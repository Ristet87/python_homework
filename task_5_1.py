# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
# yield, например:

def odd_numbers(n):
    for num in range(1, n+1, 2):
        yield num


print(list(odd_numbers(27)))

