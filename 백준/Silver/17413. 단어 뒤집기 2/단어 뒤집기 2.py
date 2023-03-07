import sys
input = sys.stdin.readline

S = map(str, input())
s_li = []
i = ""
a = ""
space = " "

for s in S:
    if s == "<":
        i = s
        if a:
            s_li.append(a[::-1])
            a = ""

    elif s == ">":
        i += s
        s_li.append(i)        
        i = ""
    
    elif i:
        i += s
    
    else:
        if s == " " or s == "\n":
            s_li.append(a[::-1])
            s_li.append(space)
            a = ""
        else:
            a += s 
print(*s_li, sep="")