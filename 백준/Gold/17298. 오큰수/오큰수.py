import sys
input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))
stack = []
answer = [-1] * n

stack.append(0)

for i in range(1, n):
    while stack and li[stack[-1]] < li[i]:
        answer[stack.pop()] = li[i]
    stack.append(i)

print(*answer)