start = input()

q = 0       # 변수 선언

if start == "고무오리 디버깅 시작":
    while True:
        N = input()
        
        if N == "고무오리 디버깅 끝":
            break
        else:
            if N == "고무오리":
                if q == 0:
                    q += 2
                else:
                    q -= 1
            elif N == "문제":
                q += 1
    if q == 0:
        print("고무오리야 사랑해")
    else:
        print("힝구")
