s = input()
n = len(s) // 10

for N in range(n+1):
    print(s[(N*10):(N*10)+10])