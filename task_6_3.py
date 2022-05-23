# names = """Иванов, Иван, Иванович
# Сергеев, Сергей, Сергеевич
# Петров, Петр, Петрович
# Сидоров, Антон, Павлович"""
#
# hobby = """рыбалка, охота
# программирование, чтение
# гитара, плавание"""
#
# with open('data/names.csv', 'w', encoding='utf-8') as f:
#     f.write(names)
#
# with open('data/hobby.csv', 'w', encoding='utf-8') as f:
#     f.write(hobby)

from itertools import zip_longest
import json

with open(r'data/names.csv', 'r', encoding='utf-8') as names:
    list_names = [name.strip() for name in names]
with open(r'data/hobby.csv', 'r', encoding='utf-8') as hobbies:
    list_hobby = [hobby.strip() for hobby in hobbies]

if len(list_names) < len(list_hobby):
    print(1)
# else:
#     final_list = dict(zip_longest(list_names, list_hobby))
#     with open('data/users_hobby.txt', 'w', encoding='utf-8') as f:
#         json.dump(final_list, f, ensure_ascii=False)
else:
    with open('data/users_hobby.txt', 'w', encoding='utf-8') as f:
        json.dump(dict(zip_longest(list_names, list_hobby)), f, ensure_ascii=False)
