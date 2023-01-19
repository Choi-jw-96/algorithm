nums_dict = {}
A = int(input())
B = int(input())
C = int(input())

for n in range(10):
    nums_dict[n] = nums_dict.get(n, 0)

for key, value in nums_dict.items():
    for abc in str(A*B*C):
        if int(abc) == key:
            value += 1
    print(value)