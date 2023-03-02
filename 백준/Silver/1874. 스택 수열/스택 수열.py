import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
num_li = deque([])
p = 0
answer = []
maxi = 0

for i in range(1, N + 1):
    num = int(input())

    if num > maxi:
        for j in range(maxi + 1, num + 1):
            num_li.append(j)
            answer.append("+")
        maxi = j
    
    if num == num_li[-1]:
        p = num_li.pop()
        answer.append("-")
    else:
        answer.append("No")

if "No" in answer:
    print("NO")
else:
    for i in answer: print(i)