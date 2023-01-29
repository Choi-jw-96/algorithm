N = int(input())


if N % 5 == 0:
        a = N // 5
        print(a)

else:
    n = 0
    while True:
        N -= 3
        n += 1
        if N <= 0:
            if N == 0:
                print(n)
                break
                
            else:
                print(-1)
            break
        if N % 5 == 0:
            a = N // 5 + n
            print(a)
            break
        