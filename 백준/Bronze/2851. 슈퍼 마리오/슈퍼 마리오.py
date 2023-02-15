score = 0
s = 0
m = 100
for _ in range(10):
    n = int(input())
    score += n
    if abs(100 - score) <= m:
        m = abs(100) - score
        s = score

print(s)