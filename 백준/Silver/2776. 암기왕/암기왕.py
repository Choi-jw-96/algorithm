for t in range(int(input())):
    see_n = int(input())
    see = sorted(list(map(int, input().split())))
    write_n = int(input())
    write = list(map(int, input().split()))
    
    for n in write:
        start, end = 0, see_n-1
        while True:
            mid = (start + end) // 2
            if see[mid] == n:
                print(1)
                break
            if start >= end:
                print(0)
                break
            if see[mid] < n:
                start = mid + 1
            else:
                end = mid - 1
                