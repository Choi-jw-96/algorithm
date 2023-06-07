import sys

n, k = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

answer = sys.maxsize

left = 0
right = 0

# 라이언 인형의 개수
one = 0

if arr[left] == 1:
    one += 1

# 왼쪽 포인터, 오른쪽 포인터 둘 중 하나가 끝에 도달할 때까지 반복한다.
while left < len(arr) and right < len(arr):
    # 라이언 인형의 개수가 부족하다면, 오른쪽 포인터를 옮겨 본다.
    if one < k:
        right += 1
        if right < len(arr) and arr[right] == 1:
            one += 1
    # 라이언 인형의 개수가 충분하다면, 왼쪽 포인터를 옮겨 본다.
    else:
        # 딱 맞게 되있다면, 사이즈를 찾아 놓는다.
        if one == k:
            answer = min(answer, right - left + 1)

        if left < len(arr) and arr[left] == 1:
            one -= 1
        left += 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)