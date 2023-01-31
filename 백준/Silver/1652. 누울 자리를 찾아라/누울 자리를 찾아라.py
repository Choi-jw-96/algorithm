N = int(input())      

room = [list(input()) for _ in range(N)]
row = 0
column = 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == ".":
            cnt += 1
            if cnt == 2:
                row += 1
                
        else:
            cnt =0


for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == ".":
            cnt += 1
            if cnt == 2:
                column += 1
                
        else:
            cnt =0
print(row, column)