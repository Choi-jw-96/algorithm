from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
li = deque([])

for _ in range(n):
    s = input().split()

    if "push_front" == s[0]:
        li.appendleft(s[1])
    elif "push_back" == s[0]:
        li.append(s[1])
    elif "pop_front" == s[0]:
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif "pop_back" == s[0]:
        if li:
            print(li.pop())
        else:
            print(-1)
    elif "size" == s[0]:
        print(len(li))
    elif "empty" == s[0]:
        if li:
            print(0)
        else:
            print(1)
    elif "front" == s[0]:
        if li:
            print(li[0])
        else:
            print(-1)
    else:
        if li:
            print(li[-1])
        else:
            print(-1)