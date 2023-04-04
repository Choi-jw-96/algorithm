T = int(input())
li = []

for _ in range(T):
    li.append(list(map(int, input().split())))

for i in range(1, T):
    for j in range(len(li[i])):
        if 0 <= j < len(li[i]) - 1:
            a = li[i-1][j]
        else:
            a = 0
        if 0<= j-1 < len(li[i]) - 1:
            b = li[i-1][j-1]
        else:
            b = 0

        li[i][j] = li[i][j] + max(a, b)
print(max(li[T-1]))