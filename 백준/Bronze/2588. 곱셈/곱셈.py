a = int(input())
b = int(input())


c = a * (b % 10)
d = a * (b % 100 // 10)
e = a * (b // 100)
t = a * b

print(c)
print(d)
print(e)
print(t)