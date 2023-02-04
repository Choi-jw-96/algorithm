N = int(input())
sosu =[]
N_list = []

for i in range(2, N + 1):
    if N % i == 0:
        n_sosu = 0

        for I in range(2, i):
            if i % I == 0:
                n_sosu += 1
                break
            
        if n_sosu == 0:
            sosu.append(i)

for i in sosu:
    while N % i == 0:
        N = N // i
        N_list.append(i)
        
print(*sorted(N_list), sep = "\n")
