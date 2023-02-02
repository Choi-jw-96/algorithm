T = int(input())

for t in range(T):
    a = int(input())
    b = int(input())
    family = []
    live = 0
    

    for i in range(1, b + 1):
        live += i
        family.append(live)

    for _ in range(1, a):
        for i in range(1, b):
            family[i] = sum(family[i-1:i+1])

    
    print(family[b-1])
