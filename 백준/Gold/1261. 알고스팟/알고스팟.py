import sys, heapq
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def go(i, j):
    visited[i][j] = 0
    queue = []
    heapq.heappush(queue, [int(miro[i][j]), i, j])

    while queue:
        wall, x, y = heapq.heappop(queue)
        if x == X - 1 and y == Y - 1:
            print(wall)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and visited[nx][ny] > wall + int(miro[nx][ny]):
                visited[nx][ny] = wall + int(miro[nx][ny])
                heapq.heappush(queue, [visited[nx][ny], nx, ny])


Y, X = map(int, input().split())

miro = [list(input()) for _ in range(X)]
visited = [[int(10e9)] * Y for _ in range(X)]

go(0, 0)