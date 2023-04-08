def dfs(l, j, i):
    global L, J, joy
    if i == n:
        if joy < j:
            joy = j
        return
    dfs (l, j, i+1)
    if l - L[i] > 0:
        dfs(l - L[i], j + J[i], i+1)
    
n = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

l, j = 100, 0

joy =0
dfs(l, j, 0)

print(joy)