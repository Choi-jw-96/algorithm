stu_list = []
no = []
for stu in range(1, 31):
    stu_list.append(stu)

for num in range(1, 29):
    nums = int(input())
    if nums in stu_list:
        stu_list.remove(nums)
print(*sorted(stu_list), sep = '\n')