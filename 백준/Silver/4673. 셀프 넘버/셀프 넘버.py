remove_set = set()
for n in set(range(1, 10001)):
    for n_1 in str(n):
        n += int(n_1)
    if n <= 10000:
        remove_set.add(n)

self_num = set(range(1, 10001)) - remove_set
print(*sorted(self_num), sep = "\n", )


