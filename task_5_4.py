# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# max_numbers = [el for el in filter(lambda x: x+1 > x, src)]
# max_numbers = [el for el in src if el[n+1] > el[n] in range(len(src))]
# max_num = []

# for el in range(len(src)-1):
#     n = src[el]
#     el += 1
#     m = src[el]
#     if m > n:
#         max_num.append(m)
#
# print(max_num)

max_num = [big for small, big in zip(src, src[1:]) if big > small]
print(max_num)