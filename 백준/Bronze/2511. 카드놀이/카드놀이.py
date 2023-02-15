A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0
last = ""

for i in range(10):
    if A[i] > B[i]:
        a += 3
        last = "A"
    elif A[i] == B[i]:
        a += 1
        b += 1
    else:
        b += 3
        last = "B"

print(a, b)
if a > b:
    print("A")
elif a == b:
    if last != "":
        print(last)
    else:
        print("D")
else:
    print("B")
