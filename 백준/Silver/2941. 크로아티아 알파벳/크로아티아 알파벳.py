s = str(input())
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0

for ap in alpha:
    if s.count(ap) >= 1:
        cnt += s.count(ap)
s_c = len(s) - cnt
print(s_c)