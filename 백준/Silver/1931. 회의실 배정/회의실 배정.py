import sys
input = sys.stdin.readline

N = int(input())
room = []

time = sorted([tuple(map(int, input().split())) for i in range(N)], key=lambda x:(x[1], x[0]))
cnt = 0
end = -1
for i in time:
    if i[0] >= end:
        cnt += 1
        end = i[1]
print(cnt)