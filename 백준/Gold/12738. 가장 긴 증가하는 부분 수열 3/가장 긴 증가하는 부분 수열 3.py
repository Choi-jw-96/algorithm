from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li_2 = [-1000000001]

for i in li:
    if li_2[-1] < i:
        li_2.append(i)
    else:
      which = bisect_left(li_2, i)
      li_2[which] = i
print(len(li_2)-1)
