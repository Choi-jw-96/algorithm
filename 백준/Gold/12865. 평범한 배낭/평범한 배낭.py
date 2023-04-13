n, k = map(int, input().split())

tool = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

bag = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j - tool[i][0] >= 0:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-tool[i][0]] + tool[i][1])
        else:
            bag[i][j] = bag[i-1][j]
print(bag[n][k])