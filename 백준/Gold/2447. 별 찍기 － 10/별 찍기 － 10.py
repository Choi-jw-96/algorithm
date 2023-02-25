import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def star(n):
    m = n // 3

    if n == 3:
        graph[1] = ["*", " ", "*"]
        graph[0][:3] = graph[2][:3] = ["*"] * 3
        return
    
    star(m)
    
    for i in range(0, n, m):
        for j in range(0, n, m):
            if i != m or j != m:
                for k in range(m):
                    graph[i + k][j : j + m] = graph[k][:m]
    


N = int(input())
graph = [[" " for _ in range(N)] for _ in range(N)]


star(N)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = "")
    print()

