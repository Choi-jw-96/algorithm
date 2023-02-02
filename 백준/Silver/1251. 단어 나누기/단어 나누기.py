i_list = []
S = input()

for s_1 in range(1, len(S)):
    for s_2 in range(s_1+1, len(S)):
        S_1 = S[:s_1]
        S_2 = S[s_1:s_2]
        S_3 = S[s_2:]
        i_list.append(S_1[::-1] + S_2[::-1] + S_3[::-1])


print(sorted(i_list)[0])