N = int(input())
n = list(map(int, input().split()))
v = int(input())

if v in n:
    print(n.count(v))
else:
    print(0)