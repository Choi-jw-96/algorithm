num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())
num9 = int(input())
nums = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
M = 0 

for n in range(9):
    if M < nums[n]:
        M = nums[n]
print(M)
print(nums.index(M) + 1)