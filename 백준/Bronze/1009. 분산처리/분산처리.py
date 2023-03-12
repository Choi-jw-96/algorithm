import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10

    if a in [1, 5, 6]:
        print(a)
        continue
    elif a == 0:
        print(10)
    elif a in [4, 9]:
        if b % 2 != 0:
            print(a)
            continue
        else:
            print((a**2)%10)
            continue
    else:
        if b % 4 == 0:
            print(a**4%10)
            continue
        else:
            print((a**(b%4))%10)
            continue    