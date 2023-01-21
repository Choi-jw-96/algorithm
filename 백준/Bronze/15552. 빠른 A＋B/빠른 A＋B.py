import sys

T = int(input())
for t in range(T):
    n_1, n_2 = map(int, sys.stdin.readline().split())
    print(n_1 + n_2)