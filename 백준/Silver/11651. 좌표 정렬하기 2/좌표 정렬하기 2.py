import sys
input = sys.stdin.readline

n = int(input())

n_li = []
for _ in range(n):
    a, b = map(int, input().split())
    n_li.append((a, b))

n_li_s = sorted(n_li, key= lambda x: (x[1], x[0]))

for _ in n_li_s:
    print(*_)
