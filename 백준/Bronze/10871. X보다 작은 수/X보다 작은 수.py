N, X = map(int, input().split())
Ns = list(map(int, input().split()))
S_Ns = []
for n in range(N):
    if Ns[n] < X:
        S_Ns.append(Ns[n])
print(*S_Ns)