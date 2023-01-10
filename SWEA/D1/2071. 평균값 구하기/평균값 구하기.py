t = int(input())
for T in range(1, t+1):
    Ns = list(map(int, input().split()))
    A = round(sum(Ns) / len(Ns))
    print(f'#{T} {A}')