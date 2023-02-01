from collections import deque
T = int(input())

for _ in range(T):
    score = list(map(int, input().split()))
    score = deque(sorted(score))
    score.pop()
    score.popleft()
    if score[2] - score[0] >= 4:
        print("KIN")
    else:
        print(sum(score))