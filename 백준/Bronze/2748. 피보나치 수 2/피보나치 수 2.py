
n = int(input())

num = 0
num_li = [0, 1]
for i in range(2, n + 1):
    num = num_li[i-2] + num_li[i-1]
    num_li.append(num)
print(num_li[n])