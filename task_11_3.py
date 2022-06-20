class OwnErr(ValueError):
    pass

list_of_int = []

while True:
    try:
        val = input("Введите число: ")
        if val == 'stop':
            print(list_of_int)
            break
        if not val.isdigit():
            raise OwnErr(val)
        list_of_int.append(int(val))
    except OwnErr as err:
        print('Вы ввели не число: ', err)
    except KeyboardInterrupt:
        print(list_of_int)
        break


