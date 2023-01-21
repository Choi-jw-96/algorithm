# [], 10 -> 입력 -> % 42 if not in append -> count
remainder = []
for t in range(10):
    num = int(input()) % 42
    if num not in remainder:
        remainder.append(num)
print(len(remainder))