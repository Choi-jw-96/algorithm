a,b = map(int, input().split())
c = int(input())
d = b + c

a += d//60
d %= 60

print(a % 24, d)