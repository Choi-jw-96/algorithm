import sys
card_n = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
s_g = list(map(int, sys.stdin.readline().split()))


from collections import Counter

count = Counter(card)


for i in s_g:
    if i in count:
        print(count[i], end = " ")
    else:
        print(0, end = " ")