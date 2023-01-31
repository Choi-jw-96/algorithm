T = int(input())

for _ in range(T):
    t_cnt = 0
    row, column = map(int, input().split())
    box = [list(map(int, input().split())) for __ in range(row)]
    box2 = [[0] * row for ___ in range(column)]

    for i in range(column):       
        for j in range(row):
            box2[i][j] = box[row - 1 - j][i]

    cnt = 0

    for b in box2:
        for i in range(len(b)):
            try:
                if b[i] == 1:
                    cnt += b[:i].count(0)
            except:
                pass
    print(cnt)