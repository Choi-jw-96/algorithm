T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    avg = sum(nums) / 10

    print(f'#{t} {round(avg)}')