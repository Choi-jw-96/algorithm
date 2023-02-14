import sys
n = int(sys.stdin.readline())
book_li = []

for _ in range(n):
    book = sys.stdin.readline().strip()
    book_li.append(book)

book_li = sorted(book_li)

from collections import Counter
count = Counter(book_li).most_common()
print(count[0][0])