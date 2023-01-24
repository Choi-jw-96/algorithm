eng_dict = {}
eng = str(input())
eng = eng.upper()
cnt = 0

for en in eng:
    if en not in eng_dict.keys():
        eng_dict[en] = 1
    else:
        eng_dict[en] += 1


for value in eng_dict.values():
    if value == max(eng_dict.values()):
        cnt += 1

if cnt >= 2:
    print("?")
else:
    print(max(eng_dict.items(), key = lambda x: x[1])[0])