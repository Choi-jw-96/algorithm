online = []
people = int(input())

pc_num = list(map(int, input().split()))

for pc in pc_num:
    if pc not in online:
        online.append(pc)

print(len(pc_num) - len(online))