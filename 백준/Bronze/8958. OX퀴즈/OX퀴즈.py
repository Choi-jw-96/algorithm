# T quiz score total
# for in quiz if o score +1 else = sc=0

# score total 위치 주의

T = int(input())

for t in range(T):
    quiz = input()
    total = 0
    score = 0
    for q in quiz:
        if q == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)
