not_self_num = []
self_num = []

for n in range(1, 10001):
    for n_1 in str(n):
        n += int(n_1)
    if n <= 10000:
        not_self_num.append(n)

for n in range(1, 10001):
    if n not in not_self_num:
        self_num.append(n)

print(*self_num, sep = "\n")