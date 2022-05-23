
parsed_tuples = []

with open(r'C:\Users\nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ip, _, __, ___, ____, get, product, *n = line.strip().split(' ')
        parsed_tuples.append((ip, get[1:], product))

print(parsed_tuples[:10])
