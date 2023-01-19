total = 0
S = input()
S = S.replace(",", " ").split()
for s in S:
    total += int(s)
print(total)
