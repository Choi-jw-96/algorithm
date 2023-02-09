b= int(input())   
paper = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(b):
    y, x = map(int, input().split())

    x = 100 - x
    
    for i in range(x - 10, x):
        for j in range(y, y + 10):
            if paper[i][j] != 1:
                paper[i][j] = 1
                cnt += 1

print(cnt)