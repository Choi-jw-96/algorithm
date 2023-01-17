N = int(input())
M  = str(N)
result = 0
cnt = 0
if len(M) == 1:
    M = "0" + M
while N != M:
    result = 0
    for m in str(M):
        result += int(m)
    for R in str(result):
        pass
    M = int(m + R)
    cnt += 1
print(cnt)