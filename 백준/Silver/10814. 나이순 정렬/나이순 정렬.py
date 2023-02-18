import sys
input = sys.stdin.readline
n = int(input())

li = []
for _ in range(n):
    age, name = input().split()
    li.append((int(age), name))

li.sort(key= lambda x: x[0])

for _ in li:
    print(*_)