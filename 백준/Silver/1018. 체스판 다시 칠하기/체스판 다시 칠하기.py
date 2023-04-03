
x, y = map(int, input().split())

graph = [list(input()) for _ in range(x)]
cnt_li = []

for X in range(x-7):
    for Y in range(y - 7):
        w = 0
        b = 0
        for i in range(X, X+8):
            for j in range(Y, Y+8):
                if (i + j) % 2 == 0:
                    if graph[i][j] != "W":
                        w += 1
                    else:
                        b += 1
                else:
                    if graph[i][j] != "W":
                        b += 1
                    else:
                        w +=1
        cnt_li.append(min(w, b))
print(min(cnt_li))