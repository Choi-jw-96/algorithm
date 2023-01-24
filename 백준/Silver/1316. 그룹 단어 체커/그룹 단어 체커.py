cnt = 0


T = int(input())

for t in range(T):
    str_input = input()
    str_list = []
    n = 0
    for s_1 in str_input:       
        if s_1 not in str_list:
            str_list.append(s_1)
        
    for s_1 in str_list:        
        if str_input.count(s_1) == 1:
            n += 1
        
        else:
            if str_input[n:n + str_input.count(s_1)] == s_1 * str_input.count(s_1):
                n += str_input.count(s_1)
            else:
                cnt += 1
                break
print(T - cnt)