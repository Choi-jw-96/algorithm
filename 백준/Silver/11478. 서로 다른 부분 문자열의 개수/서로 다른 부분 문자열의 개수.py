import sys
input = sys.stdin.readline
s = input().strip()
dic = {} 

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j] not in dic:
            dic[s[i:j]] = 1
        else:
            dic[s[i:j]] += 1

print(len(dic))