# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

unique_num = set()
temp_num = set()

for el in src:
    if el not in temp_num:
        unique_num.add(el)
    else:
        unique_num.discard(el)
    temp_num.add(el)

print(unique_num)

src_2 = [el for el in src if el in unique_num]
print(src_2)