w = [int(input()) for W in range(10)]
k = [int(input()) for K in range(10)]

# 내림차순으로 정렬
w = sorted(w, reverse = True)
k = sorted(k, reverse = True)

# 0~2까지 슬라이스한 합
print(sum(w[:3]), sum(k[:3]))