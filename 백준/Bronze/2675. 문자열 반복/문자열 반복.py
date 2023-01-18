t = int(input())
for T in range(t):
    num, s = map(str, input().split())
    pint =""

    for S in s:
        S_ = S * int(num)
        pint += S_
    print(pint)
