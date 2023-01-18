t = int(input())

for T in range(t):
    s = list(map(str, input().split()))
    for S in s:
        S = S[::-1]
        print(S, end = " ")