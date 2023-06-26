# 두 원의 중심 반지름을 입력했을 때 접점을 구하는 문제
# 공식이 필요한 문제
import math

for i in range(int(input())):
    jx, jy, r1, bx, by, r2= map(int, input().split())
    # math.pow(x, y) 함수는 x의 y 거듭제곱 (x의 y승)을 반환 (x가 음수 y가 실수면 error)
    # math.sqrt(x) 함수는 x의 제곱근을 반환 (음수가 나오면 error)
    distance = math.sqrt((jx - bx) ** 2 + (jy - by)**2)
    # 원의 중심이 같을때
    if distance == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 == distance or abs(r2 - r1) == distance:
            print(1)
        elif (abs(r2 - r1) < distance and (distance < r1 + r2)):
            print(2)
        else:
            print(0)