N, K = map(int, input().split())

li=[]
li_2 = []

for i in range(1, N + 1):
    li.append(i)

k = K -1
while li:    
    if k >= len(li):
        while k >= len(li):
            k -= len(li)
        li_2.append(str(li.pop(k)))
        k -= 1
    else:
        li_2.append(str(li.pop(k)))
        k -= 1
    k += K
print("<%s>" %(", ".join(li_2)))