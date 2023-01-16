t_case = int(input())
for T_case in range(1, t_case+1):
    num_1, num_2 = map(int, input().split())
    add = num_1 + num_2
    print(f"Case #{T_case}: {num_1} + {num_2} = {add}")