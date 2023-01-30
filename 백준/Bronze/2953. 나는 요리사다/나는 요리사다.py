P = []
t = 0 
num = 0
for _ in range(5):
    p = list(map(int, input().split()))
    P.append(p)
for i in range(5):
    
    if t < sum(P[i]):
        t = sum(P[i])
        num = i + 1
print(num, t)