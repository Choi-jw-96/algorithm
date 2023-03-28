import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = []

high = -1
low = 260

for _ in range(N):
    n =list(map(int, input().split())) 
    graph.append(n)
    high = max(max(n), high)
    low = min(min(n), low)

short_time = int(1e9)
ground = 0
for i in range(low, high + 1):
    inven = 0
    plant = 0
    for x in graph:
        for j in x:
            if j > i:
              inven += j - i
            else:
              plant += i - j
    
    if inven + B < plant:
       continue
    else:
       time = (inven * 2) + plant
       if short_time >= time:
          short_time = time
          ground = i
print(short_time, ground)