import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))

li_sorted = sorted(li, key = lambda x: (x[0], x[1]))

for i in li_sorted:
    print(*i)
