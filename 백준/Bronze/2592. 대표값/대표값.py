nums = [int(input()) for _ in range(10)]

print(sum(nums) // len(nums))

c = 0
for i in nums:
    cnt = 0
    for j in nums:
        if i == j:
            cnt += 1
    if c < cnt:
        c = cnt
        mode = i

print(mode)