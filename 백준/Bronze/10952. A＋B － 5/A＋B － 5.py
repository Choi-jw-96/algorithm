A, B = 1, 1
while A >= 1 and B <= 9:
    A, B = map(int, input().split())
    add = A + B
    if add == 0:
        add = ""
    print(add)