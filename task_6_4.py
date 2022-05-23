
from itertools import zip_longest
import json

with open(r'data/names.csv', 'r', encoding='utf-8') as names:
    list_names = [name.strip() for name in names]
with open(r'data/hobby.csv', 'r', encoding='utf-8') as hobbies:
    list_hobby = [hobby.strip() for hobby in hobbies]

with open('data/users_hobby.txt', 'w', encoding='utf-8') as f:
    for name, hobby in zip_longest(list_names, list_hobby):
        f.write(f'{name}: {hobby}\n')
