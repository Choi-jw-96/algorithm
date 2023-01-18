nums = list(map(int, input().split()))

while nums != sorted(nums):
    for i in range(4):
        if nums[i] > nums[i+1]:
            num = nums[i]
            nums.pop(i)
            nums.insert(i+1, num)
            print(*nums)