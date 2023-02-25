def move(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        move(n-1, a, c, b )
        print(a, c)
        move(n-1, b, a, c)


N = int(input())

count = 0
for _ in range(N):
    count = count * 2 + 1

print(count)
move(N, 1, 2, 3)