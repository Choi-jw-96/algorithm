N, K = map(int, input().split())
A = list(map(int, input().split(",")))

for i in range(K):
    for j in range(len(A)):
        if j == len(A) - 1:
            A.pop(j)
        else:
            A[j] = A[j + 1] - A[j]

print(*A, sep=",")