nums = list(map(int, input().split()))
min_num = min(nums)

while True:
    cnt = 0
    for i in nums:
        if min_num % i == 0:
            cnt += 1

        if cnt == 3:
            print(min_num)
            exit()
    min_num += 1