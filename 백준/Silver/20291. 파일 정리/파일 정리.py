import sys
n = int(sys.stdin.readline())

file_li = []
for i in range(n):
    file = sys.stdin.readline().strip()
    file_li.append(file[file.find(".") + 1:])


from collections import Counter
file_li = Counter(file_li).most_common()

file_li = sorted(file_li)

for _ in file_li:
    print(*_)