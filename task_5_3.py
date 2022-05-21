from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_gen = (zip_longest(tutors, klasses) if len(tutors) >= len(klasses) else zip(tutors, klasses))
print(*tutors_gen)

# def tutors_gen(*args):
#     if len(tutors) >= len(klasses):
#         yield tuple(zip_longest(*args))
#     else:
#         yield tuple(zip(*args))
#
# print(*tutors_gen(tutors, klasses))