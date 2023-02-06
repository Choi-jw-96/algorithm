desktop = int(input())
link = int(input())

graph = [ [] for _ in range(desktop + 1)]

for _ in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited= [False] * (desktop + 1)

def dfs(start):
    stack=[start]
    visited[start] = True
    
    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

dfs(1)

cnt = 0

for _ in visited:
    if _ == True:
        cnt += 1
print(cnt - 1)