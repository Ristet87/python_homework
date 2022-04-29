
list_of_price = [57.8, 46.51, 97, 101, 65.02, 33.50, 75, 98.1, 0.75, 10]
list_of_floats = []
price_list = []
final_list = []
for price in list_of_price:
    list_of_floats.append(str(float(price)))
print(list_of_floats)
for i in list_of_floats:
    price_list = i.split('.')
    price_list_1 = f'{int(price_list[0])} руб {int(price_list[1]):02d} коп'
    print(price_list_1)
    final_list.append(price_list_1)
print(final_list)
