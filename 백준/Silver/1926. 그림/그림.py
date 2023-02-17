dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

big = 0
def dfs(graph, x, y, visited):
    global big, c
    big = max(big, visited[x][y])
    c += 1

    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = c
                dfs(graph, nx, ny, visited)
    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
vitised = [[0] * m for _ in range(n)]

pic = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            if vitised[x][y] == 0:
                c = 1
                vitised[x][y] = 1
                dfs(graph, x, y, vitised)
                pic += 1
                

print(pic)
print(big)