S = str(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
# cnt = []

for ap in alpha:
    # cnt.append(S.find(ap))
#print(*cnt)
    print(S.find(ap), end = " ")

# ## 아스키 버전
# alpha = range(97, 123)

# for ap in alpha:
#     print(S.find(chr(ap)), end =" ")