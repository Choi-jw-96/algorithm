s = str(input())

for A in ["C", "A", "M", "B", "R", "I", "D", "G", "E"]:
    if s.find(A) == -1:
        pass
    else:
         s = s.replace(A,"")

print(s)