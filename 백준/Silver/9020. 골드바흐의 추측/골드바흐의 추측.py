sosu = []
for i in range(2, 10000):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosu.append(i)

for _ in range(int(input())):
    n = int(input())
    
    for i in range(len(sosu)):
        if n // 2 == sosu[i]:
            break
        if n // 2 < sosu[i]:
            i -= 1
            break
    
    stop = 0
    for num_1 in sosu[i :  : -1]:
        if stop > 0:
            break
        for num_2 in sosu[i : ]:
            if n == num_1 + num_2:
                print(num_1, num_2)
                stop = 1
                break