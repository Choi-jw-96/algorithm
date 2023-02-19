import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
X = list(map(int, input().split()))

x_c = sorted(set(X))

X_dict = {}
for i in range(len(x_c)):
    X_dict[heapq.heappop(x_c)] = i

for j in X:
    print(X_dict[j], end = " ")