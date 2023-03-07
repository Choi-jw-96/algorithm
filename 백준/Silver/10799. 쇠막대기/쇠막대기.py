import sys
input = sys.stdin.readline

stick = list(input().strip())

cut = 0
total = []
st_c = 0

for i in range(len(stick)):
    if stick[i] == "(":
        total.append(stick[i])
    else:
        if stick[i-1] == "(":
            total.pop()
            if total:
                st_c += len(total)
        else:
            total.pop()
            st_c += 1


print(st_c)