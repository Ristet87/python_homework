task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
final_list = []
for i in task_list:
    if i.isdigit() == True:
        final_list.extend(['"', f'{int(i):02d}', '"'])
    elif i[0] == '+' or i[0] == '-':
        final_list.extend(['"', f'{i[0]}{int(i[1:]):02d}', '"'])
    else:
        final_list.append(i)
print(final_list)
final_list_1 = ' '.join(final_list)
print(final_list_1)