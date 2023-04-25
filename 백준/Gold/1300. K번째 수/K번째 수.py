n = int(input())
k = int(input())

start, end = 1, n*n

while start <= end:
  mid = (start + end) // 2
  num = 0    
  for i in range(1, n+1):
    num += min(n, mid//i)
  if num < k:
    start = mid + 1
  else:
    K = mid
    end = mid - 1
print(K)