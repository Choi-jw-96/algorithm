office = {}

T = int(input())

for t in range(T):
    human, work = map(str, input().split())
    office[human] = work
for key in sorted(office.keys(), reverse= True):
    if office[key] == "enter":
        print(key)