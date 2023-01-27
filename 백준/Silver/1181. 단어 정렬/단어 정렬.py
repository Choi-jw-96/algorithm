Ns = []
a = int(input())
for _ in range(a):
    Ns.append(input())

Ns = set(Ns)
Ns = sorted(list(Ns))   # 오름차순 먼져 정렬
Ns = sorted(Ns, key= len)   # 글자 수대로 정렬

print(*Ns, sep = "\n")