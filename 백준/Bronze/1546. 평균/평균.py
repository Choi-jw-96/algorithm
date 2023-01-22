# M N totla
# 입력 M을 골라 for /70* total +=
# /N

N = int(input())
total = 0
score = list(map(int, input().split()))

for s in score: 
    total += s / max(score) * 100

print(total / N)
