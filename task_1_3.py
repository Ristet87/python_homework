num = int(input('Введите число: '))
if 1 == num or (num > 20 and num % 10 == 1):
    print(num, 'процент')
elif 1 < num < 5 or num > 20 and 1 < num % 10 < 5:
    print(num, 'процента')
else:
    print(num, 'процентов')

