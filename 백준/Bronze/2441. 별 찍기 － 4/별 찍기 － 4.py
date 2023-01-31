n = int(input())

star = [[] * n for _ in range(n)]

for i in range(n):
    star[i] = [" " * i + "*" * (n - i)]
    print(*star[i])