k, n = map(int, input().split())

li = [i for i in range(1, k + 1)]
li_2 = []
m = n - 1
while li:
    if m >= k:
        m = m % k
    li_2.append(li.pop(m))
    m += n - 1
    k -= 1
print('<', end='')
for i in range(len(li_2)-1):
    print(li_2[i], end=', ')
print(li_2[-1], end='')
print('>')