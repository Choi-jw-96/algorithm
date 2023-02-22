def su(a, b):
    global cnt
    cnt += 1
    if N == 0:
        return print(0)
    if cnt == N:
        print(b)
    else:
        c = a + b
        su(b, c)

N = int(input())
cnt = 0
su(0, 1)