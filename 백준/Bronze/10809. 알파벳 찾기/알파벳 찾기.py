S = str(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
# cnt = []

for abc in alpha:
    # cnt.append(S.find(abc))
#print(*cnt)
    print(S.find(abc), end = " ")

# ## 아스키 버전
# alpha = range(97, 123)

# for abc in alpha:
#     print(S.find(chr(abc)), end =" ")