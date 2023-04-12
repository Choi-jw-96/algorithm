import sys
input = sys.stdin.readline

k, n = map(int, input().split())
li = []
for i in range(k):
    li.append(int(input()))

short, long = 1, max(li)

while short <= long:
    cut = (long + short) // 2
    lines = 0
    for i in li:
        lines += i // cut
    
    if lines >= n:
        short = cut + 1
    else:
        long = cut - 1
print(long)