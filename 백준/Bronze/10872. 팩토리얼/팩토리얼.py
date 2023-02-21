N = int(input())

def d(n):
    if n == 0:
        return 1
    return n * d(n-1)

print(d(N))