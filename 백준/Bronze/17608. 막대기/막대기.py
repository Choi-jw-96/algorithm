import sys
stick = int(input())
stick_list = []
cnt = 0

for _ in range(stick):
    stick_list.append(int(sys.stdin.readline()))

stick_h = 0

for i in range(stick-1 , -1, -1):
    if stick_list[i] > stick_h:
        stick_h = stick_list[i]
        cnt += 1

print(cnt)