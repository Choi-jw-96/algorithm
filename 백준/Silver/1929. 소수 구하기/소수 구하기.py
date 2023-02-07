import sys
M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    n_sosu = 0
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i == 2:
            print(i)
            break
        
        elif i % j == 0:
            n_sosu += 1
            break
                
    if n_sosu == 0:
        print(i)