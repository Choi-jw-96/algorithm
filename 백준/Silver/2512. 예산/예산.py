import sys
input = sys.stdin.readline

n = int(input())
tax = list(map(int, input().split()))
limit = int(input())

start, end = 0, max(tax)

if sum(tax) > limit:
  while start <= end:
      total_tax = 0
      mid = (start + end) // 2
      for i in tax:
          total_tax += min(mid, i)
      if limit >= total_tax:
          start = mid + 1
      else:
          end = mid -1
print(end)