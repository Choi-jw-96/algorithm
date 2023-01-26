jangbu_list = []
T = int(input())

for t in range(T):
    num = int(input())
    if num == 0:
        jangbu_list.pop()
    else:
        jangbu_list.append(num)
print(sum(jangbu_list))