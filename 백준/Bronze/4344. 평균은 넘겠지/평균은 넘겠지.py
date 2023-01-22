T = int(input())

for t in range(T):
    cla = list(map(int, input().split()))

    avg = (sum(cla) - cla[0])/ cla[0]
    cnt = 0

    for stu in cla[1:]:
        
        if stu > avg:
            cnt += 1
    print(f'{(cnt / cla[0] * 100):.3f}%')      
    # 소수점 표시 주의  