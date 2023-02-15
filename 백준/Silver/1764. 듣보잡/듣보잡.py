import sys
a, b = map(int, sys.stdin.readline().split())

N = set()
M = set()

for _ in range(a):
    N.add(sys.stdin.readline().strip())

for _ in range(b):
    M.add(sys.stdin.readline().strip())

print(len((N & M)), *sorted(N & M), sep = "\n")  