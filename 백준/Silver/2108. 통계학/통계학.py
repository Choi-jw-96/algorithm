import sys, math
n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

s_n = sorted(nums)

avg = round(sum(nums)/n)
mid = s_n[math.ceil(len(nums)//2)]

cnt = {}
for i in range(len(s_n)):
    if s_n[i] not in cnt:
        cnt[s_n[i]] = 1
    else:
        cnt[s_n[i]] += 1

same = []

for key, value in cnt.items():
    if value == max(cnt.values()):
        same.append(key)

if len(same) == 1:
    look = same[0]
else:
    look = same[1]
    
side = s_n[len(nums)-1]- s_n[0]
print(avg, mid, look, side, sep = "\n")