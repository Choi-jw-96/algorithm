import sys
num = sys.stdin.readline().strip()

num_dict ={}
for n in num:
    if int(n) not in num_dict:
        num_dict[int(n)] = 1
    else:
        num_dict[int(n)] += 1

for i in range(9, -1, -1):
    if i in num_dict:
        print(str(i) * num_dict[i], end = "")