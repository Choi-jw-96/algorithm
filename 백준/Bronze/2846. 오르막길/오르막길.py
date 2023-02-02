n = int(input())
h = list(map(int, input().split()))
H = 0
H_list = []

for i in range(n):
    try:
        if h[i + 1] - h[i] > 0:
            H += h[i + 1] - h[i]
        
        else:
            H_list.append(H)
            H = 0

    except:
        H_list.append(H)
print(max(H_list))