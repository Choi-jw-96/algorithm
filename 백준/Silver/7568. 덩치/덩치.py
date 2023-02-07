people = int(input())
people_list = []

for _ in range(people):
    x = list(map(int, input().split()))
    people_list.append(x)

h = []
for i in range(people):
    cnt = 0

    for j in range(people):
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            cnt += 1
    h.append(cnt + 1)


print(*h)