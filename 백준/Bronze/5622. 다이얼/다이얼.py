tel = {2 : "ABC", 3 : "DEF", 4 : "GHI", 5 : "JKL", 
6 : "MNO", 7 : "PQRS", 8 : "TUV", 9 : "WXYZ"}

phone = input()
time = 0

for P in phone:
    for num, alpha in tel.items():
        if P in alpha:
            time += num + 1
            break
print(time)