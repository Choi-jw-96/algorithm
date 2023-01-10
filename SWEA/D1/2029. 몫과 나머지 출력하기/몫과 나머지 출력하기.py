t = int(input())
for T in range(1, t+1):
    a, b = map(int, input().split())
    c = a // b
    d = a % b
    print(f"#{T} {c} {d}")
