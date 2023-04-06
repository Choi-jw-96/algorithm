N = int(input())
li = []
for _ in range(N):
    T, P = map(int, input().split())
    li.append((T, P))

money = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + li[i][0] <= N:
        money[i] = max(money[i+1], li[i][1] + money[i+li[i][0]])
    else:
        money[i] = money[i+1]
print(money[0])