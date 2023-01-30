import sys
A, B = map(str, sys.stdin.readline().split())
total = 0

A= list(A)
B = list(map(int, B))
 
for a in A:
    add = int(a) * sum(B)
    total += add
print(total)