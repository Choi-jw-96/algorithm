n = int(input())
stair = [0]
score = [0] * (n+1)
for i in range(n):
  stair.append(int(input()))
  if i < 2:
    score[i+1] = sum(stair[0:i+2])

for i in range(3, n+1):
    score[i] = max(score[i-2]+stair[i], score[i-3]+stair[i-1]+stair[i])
print(score[-1])