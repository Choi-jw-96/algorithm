def dfs(x):
    global Queen
    if x == n:
        Queen += 1
        return
    
    for y in range(n):
        if not visited_1[y] and not visited_2[x+y] and not visited_3[x-y]:
            visited_1[y] = visited_2[x+y] = visited_3[x-y] = 1
            dfs(x+1)
            visited_1[y] = visited_2[x+y] = visited_3[x-y] = 0
    

n = int(input())

visited_1 = [0] * n
visited_2 = [0] * (2 * n)
visited_3 = [0] * (2 * n)
Queen = 0
dfs(0)
print(Queen)