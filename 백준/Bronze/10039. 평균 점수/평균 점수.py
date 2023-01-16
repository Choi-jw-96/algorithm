stu_1 = int(input())
stu_2 = int(input())
stu_3 = int(input())
stu_4 = int(input())
stu_5 = int(input())
stu_total = 0
stu_list = [stu_1, stu_2, stu_3, stu_4, stu_5]

for N in range(5):
    if stu_list[N] < 40:
        stu_total += 40
    else:
        stu_total += stu_list[N]

stu_avg = stu_total / len(stu_list)
print(int(stu_avg))