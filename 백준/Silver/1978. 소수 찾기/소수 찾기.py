T = int(input())
nums = list(map(int, input().split()))
sosu = []

for num in nums:
    if num == 1 or num % 2 == 0:
        if num == 2:
            sosu.append(num)
        continue
    else:
        if num == 3 or 5: 
            sosu.append(num)
        for n in range(2, num//2):
            if num % n == 0:
                if num in sosu:
                    sosu.pop()
                break
            else:
                if num not in sosu:
                    sosu.append(num)
print(len(sosu))