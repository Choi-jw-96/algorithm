# DFS
def dfs(grap, v, visit):
    visit[v] = True
    DFS.append(v)

    for i in sorted(grap[v]):       
        if not visit[i]:
            dfs(grap, i, visited)

# BFS
from collections import deque
def bfs(grap, v, visit):

    queue = deque([v])

    visit[v] = True
    while queue:
        n = queue.popleft()
        BFS.append(n)
        for i in sorted(grap[n]):
            if not visit[i]:
                visit[i] = True
                queue.append(i)



N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [[] for _ in range(N + 1)]
visited_2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS = []
BFS = []

dfs(graph, V, visited)
bfs(graph, V, visited_2)


print(*DFS)
print(*BFS)