import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(start):
    global cnt
    visited[start] = True
    cnt += 1

    for _ in range(2):
        if _ == 0:
            newstart = start + stone[start]
        else:
            newstart = start - stone[start]
        
        if 0 <= newstart < n and not visited[newstart]:
            DFS(newstart)


n = int(input())
stone = list(map(int, input().split()))
start = int(input())

visited = [False] * n
cnt = 0
DFS(start-1)

print(cnt)