N = int(input())

for n in reversed(range(4, N + 1)):
    ok = 0
    for i in range(len(str(n))):
        if str(n)[i] == "4" or str(n)[i] == "7":
            ok += 1
        else:
            break

    if ok == len(str(n)):
        print(n)
        break