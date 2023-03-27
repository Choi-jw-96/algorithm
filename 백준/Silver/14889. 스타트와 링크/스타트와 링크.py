from itertools import permutations, combinations
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# p = permutations(range(0, N), N//2)
p = list(combinations(range(N), N//2))
# print(list(p))
A = []
B = []

for i in range(len(p)//2):
    A.append(p[i])
    B.append(p[-i-1])

min_score = float('inf')
for i in range(len(A)):
    a_score, b_score = 0, 0
    for j in range(len(A[i])-1):
        for k in range(j, len(p[i])):
            a_score += graph[A[i][j]][A[i][k]] + graph[A[i][k]][A[i][j]]
            b_score += graph[B[i][j]][B[i][k]] + graph[B[i][k]][B[i][j]]
    if min_score > abs(a_score - b_score):
        min_score = abs(a_score - b_score)
print(min_score)