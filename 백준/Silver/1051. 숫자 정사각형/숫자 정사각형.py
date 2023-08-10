import sys
input = sys.stdin.readline

N, M = map(int, input().split())
square= []

for i in range(N):
    square.append(list(input().strip()))

min_line = min(N, M)
size = 1
for i in range(N):
    for j in range(M):
        # 정사각형을 만들기 위해 N, M 둘 중 짧을 것을 체크
        for k in range(1, min_line):
            # 정사각형 조건이 되면서, 각 꼭지점의 크기가 같을 때
            if i + k < N and j + k < M :
              if square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]:
                  size = max(size, (k+1)**2)
print(size)