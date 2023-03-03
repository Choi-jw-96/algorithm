from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = deque([])
for _ in range(n):
    s = input().split()

    if "push" in s:
        li.append(s[1])
    elif "pop" in s:
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif "size" in s:
        print(len(li))
    elif "empty" in s:
        if li:
            print(0)
        else:
            print(1)
    elif "front" in s:
        if li:
            print(li[0])
        else:
            print(-1)
    else:
        if li:
            print(li[-1])
        else:
            print(-1)